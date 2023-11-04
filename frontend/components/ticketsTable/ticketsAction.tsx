// TicketActions.tsx
import React from 'react';
import Button from '@mui/material/Button';
import DeleteIcon from '@mui/icons-material/Delete';
import RestoreIcon from '@mui/icons-material/Restore';

interface TicketActionsProps {
  id: string;
  handleDiscardChanges: (id: string) => void;
  handleDelete: (id: string) => void;
  edited: boolean;
  deleted: boolean;
}

const TicketActions: React.FC<TicketActionsProps> = ({
  id,
  handleDiscardChanges,
  handleDelete,
  edited,
  deleted,
}) => {
  return (
    <>
      <Button
        variant="contained"
        size="small"
        startIcon={<RestoreIcon />}
        onClick={() => handleDiscardChanges(id)}
        disabled={!edited && !deleted}
      />
      <Button
        variant="contained"
        size="small"
        startIcon={<DeleteIcon />}
        onClick={() => handleDelete(id)}
        disabled={deleted}
      />
    </>
  );
};

export default TicketActions;
