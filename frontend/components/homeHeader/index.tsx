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
        <Box display="flex" flexGrow={0}>
          <Link href="/"><Button color="inherit" sx={{ mr: 5 }}>Messages</Button></Link> {/* Margin right */}
          <Link href="/"><Button color="inherit" sx={{ mr: 5 }}>Tasks</Button></Link> {/* Margin right */}
          <Link href="/home"><Button variant="contained">Dashboard</Button></Link>
        </Box>

      </Toolbar>
    </AppBar>
  );
};

export default HomeHeader;
