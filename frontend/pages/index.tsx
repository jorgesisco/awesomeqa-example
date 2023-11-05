import { styled } from "@mui/material/styles";
import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import { Button } from "@mui/material";
import Link from 'next/link';
import CustomButton from '../components/PageButton'
import DashboardIcon from '@mui/icons-material/Dashboard';


const IndexPage = () => {
  return (
    <Box sx={{ flexGrow: 1, mt: 15, mb: 15, display: "flex", height:"50vh"}}>
    {/* <Box sx={{ flexGrow: 1, mt: 15, mb: 15, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "50vh" }}> */}
      <Grid container justifyContent="center" alignItems="center">
        <Grid item xs={12} md={3}>
          <Box sx={{ display: "flex", justifyContent: "center" }}>
            <Link href="/home"><CustomButton Icon={DashboardIcon} label="Go to Dashboard"/></Link>
          </Box>
        </Grid>
     
      </Grid>
    </Box>
  );
};

export default IndexPage;
