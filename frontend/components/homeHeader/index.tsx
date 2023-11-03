import React from 'react';
import { AppBar , Toolbar, Button} from '@mui/material';
import { Box, Typography } from "@mui/material";
import Link from 'next/link';
const HomeHeader = () => {
  return (
    <AppBar position="static" color="transparent" elevation={0}>
      <Toolbar>
        
        <Box display="flex" flexGrow={1}>
        <Link href='/'>
          <Typography variant="h6" component="div" sx={{ cursor: 'pointer' }}>
            AwesomeQA
          </Typography>
          </Link>
        </Box>
        
        <Button color="inherit" href="/about">Messages</Button>
        <Button color="inherit" href="/pricing">Tasks</Button>
        <Button variant="contained" href="/dashboard">Dashboard</Button>
      </Toolbar>
    </AppBar>
  );
};

export default HomeHeader;
