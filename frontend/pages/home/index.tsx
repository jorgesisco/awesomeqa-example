import * as React from "react";
import { NextPage } from "next";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import Link from 'next/link';
import CustomButton from '../../components/PageButton';
import ArticleOutlinedIcon from '@mui/icons-material/ArticleOutlined'; // Sample icon
import SupportAgentOutlinedIcon from '@mui/icons-material/SupportAgentOutlined'; // Sample icon
import LightbulbOutlinedIcon from '@mui/icons-material/LightbulbOutlined'; // Sample icon
const Home: NextPage = () => {

  const handleClick = async () => {
    console.log("clicked");
  };

  return (
    <Box sx={{ flexGrow: 1, mt: 15, mb: 15, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "50vh" }}>
      <Grid container spacing={-60} justifyContent="center" alignItems="center">
      
        <Grid item xs={12} md={4}>
          <Box sx={{ display: "flex", justifyContent: "center" }}>
          <Link href="/knowledge"><CustomButton Icon={ArticleOutlinedIcon} label="Knowledge Base"/></Link>
          </Box>
        </Grid>
        <Grid item xs={12} md={4}>
          <Box sx={{ display: "flex", justifyContent: "center" }}>
          <Link href="/tickets"><CustomButton Icon={SupportAgentOutlinedIcon} label="Tickets" /></Link>
          </Box>
        </Grid>
        <Grid item xs={12} md={4}>
          <Box sx={{ display: "flex", justifyContent: "center" }}>
          <Link href="/faq"><CustomButton Icon={LightbulbOutlinedIcon} label="FaQ Insights"/></Link>
          </Box>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Home;
