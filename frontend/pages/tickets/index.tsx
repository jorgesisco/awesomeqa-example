import * as React from "react";
import { NextPage } from "next";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import TicketsTable from "../../components/ticketsTable";


const tickets: NextPage = () => {

  const handleClick = async () => {
    console.log("clicked");
  };
  
  return (
    <>
      <Box sx={{ flexGrow: 1, mt: 15, mb: 15 }}>
        <Grid container spacing={3} justifyContent="center">
          <Grid item xs={12}>
            <Box sx={{ display: "flex", justifyContent: "center", height: 750, maxWidth: '100%' }}>
            <TicketsTable />
            </Box>
          </Grid>
        </Grid>
      </Box>
    </>
  );
};

export default tickets;
