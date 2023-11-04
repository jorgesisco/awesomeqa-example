import React, { useState, useEffect, useRef } from 'react';
import { DataGrid, GridRowsProp, GridColDef, GridToolbar } from '@mui/x-data-grid';
import { fetchTickets } from '../../hooks/userTickets';
import Button from '@mui/material/Button';
import TicketActions from '../../components/ticketsTable/ticketsAction';

interface Ticket {
  id: string;
  status: string;
  resolved_by: string | null;
  timestamp: string;
  message_content: string;
  message_link: string;
}

const TicketsTable: React.FC = () => {
  const [rows, setRows] = useState<GridRowsProp>([]);
  const originalRowsRef = useRef<GridRowsProp>([]);
  const [hasUnsavedRows, setHasUnsavedRows] = useState(false);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState(null);

  // Track which rows have been edited or marked for deletion
  const [editedRows, setEditedRows] = useState<Record<string, any>>({});
  const [deletedRows, setDeletedRows] = useState<Record<string, boolean>>({});

  const handleDelete = (id) => {
    // Mark row as deleted but keep it in the state
    setDeletedRows((prev) => ({ ...prev, [id]: true }));
    setHasUnsavedRows(true);
  
    // Optionally, you can also update local storage immediately
    const updatedRows = rows.filter((row) => row.id !== id);
    localStorage.setItem('tickets', JSON.stringify(updatedRows));
  };

  const handleDiscardChanges = (id) => {
    // Restore original row state
    const originalRow = originalRowsRef.current.find((row) => row.id === id);
    if (originalRow) {
      setRows((prevRows) =>
        prevRows.map((row) => (row.id === id ? originalRow : row))
      );
    }
  
    // Update the state of editedRows and deletedRows first
    setEditedRows((prev) => {
      const updated = { ...prev };
      delete updated[id];
      return updated;
    });
  
    setDeletedRows((prev) => {
      const updated = { ...prev };
      delete updated[id];
      return updated;
    });
  
    // Since setState actions are asynchronous, use a callback for hasUnsavedRows to ensure
    // we get the latest state of editedRows and deletedRows
    setHasUnsavedRows((prevHasUnsavedRows) => {
      // Compute if there are any edited or deleted rows after the updates
      const hasEdited = Object.keys(editedRows).length > 0;
      const hasDeleted = Object.keys(deletedRows).length > 0;
  
      // Check against previous state inside the updater function
      const isAnyEditedRowLeft = hasEdited && !editedRows.hasOwnProperty(id);
      const isAnyDeletedRowLeft = hasDeleted && !deletedRows.hasOwnProperty(id);
  
      return isAnyEditedRowLeft || isAnyDeletedRowLeft;
    });
  };

  useEffect(() => {
    const hasEdited = Object.keys(editedRows).length > 0;
    const hasDeleted = Object.keys(deletedRows).length > 0;
    setHasUnsavedRows(hasEdited || hasDeleted);
  }, [editedRows, deletedRows]);
  

  const saveChanges = () => {
    // Filter out the deleted rows
    const updatedRows = rows.filter((row) => !deletedRows[row.id]);
    
    // Update the rows state
    setRows(updatedRows);
    
    // Update the local storage with the updated rows
    localStorage.setItem('tickets', JSON.stringify(updatedRows));
    
    // Clear the edited and deleted state
    setEditedRows({});
    setDeletedRows({});
    setHasUnsavedRows(false);
  };

  const columns: GridColDef[] = [
    // ... other columns definitions
    {
      field: 'actions',
      headerName: '',
      width: 150,
      renderCell: (params) => (
        <TicketActions
          id={params.id.toString()}
          handleDiscardChanges={handleDiscardChanges}
          handleDelete={handleDelete}
          edited={Boolean(editedRows[params.id])}
          deleted={Boolean(deletedRows[params.id])}
        />
      ),
      sortable: false,
      filterable: false,
    },
    { field: 'id', headerName: 'Ticket ID', width: 100 },
    // { field: 'msg_id', headerName: 'Message ID', width: 150 },
    { field: 'status', headerName: 'Status', width: 80 },
    { field: 'resolved_by', headerName: 'Resolved By', width: 100 },
    { field: 'timestamp', headerName: 'Created Date', width: 180 },
    { field: 'message_content', headerName: 'Message', width: 500 },
    // { field: 'message_link', headerName: 'Message Link', width: 180 },
    {
        field: 'message_link',
        headerName: 'Message Link',
        width: 120,
        renderCell: (params) => (
          <a href={params.value} target="_blank" rel="noopener noreferrer" style={{textDecoration: 'underline' }}>
          See message
        </a>
        ),
      }
  ];

  useEffect(() => {
    const url = 'http://0.0.0.0:5001/tickets';
    const savedTickets = localStorage.getItem('tickets');
    
    if (savedTickets) {
        setRows(JSON.parse(savedTickets));
        setLoading(false);
    } else{
        setLoading(true);

    fetchTickets(url)
    .then(data => {
        const ticketsData: Ticket[] = data.map((ticket: any) => ({
            id: ticket.id,
            msg_id: ticket.msg_id,
            status: ticket.status,
            resolved_by: ticket.resolved_by || 'N/A', // Fallback to 'N/A' if null
            timestamp: new Date(ticket.timestamp).toLocaleString(), // Format the timestamp
            message_content: ticket.message.content,
            message_link: ticket.message.msg_url
          }));

        // Save to local storage if the data is valid
        if (ticketsData.length > 0) {
            localStorage.setItem('tickets', JSON.stringify(ticketsData));
        }
        
        setRows(ticketsData); // Transform data here if needed
        setLoading(false);
    })
    .catch(error => {
        setError(error);
        setLoading(false);
    });
    }
}, []);

  return (
    <div style={{ height: 550, width: '100%' }}>
      <div style={{ marginBottom: 8 }}>
        <Button
          variant="contained"
          onClick={saveChanges}
          disabled={!hasUnsavedRows}
          color="primary"
        >
          Save All Changes
        </Button>
      </div>
      <DataGrid
        rows={rows}
        columns={columns}
        loading={loading}
        slots={{ toolbar: GridToolbar }}
      />
      
      {error && <div style={{ color: 'red' }}>Error: {error.message}</div>}
    </div>
  );
};

export default TicketsTable;
