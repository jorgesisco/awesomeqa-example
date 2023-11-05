import React from 'react';
import Button, { ButtonProps } from '@mui/material/Button';
import Box from '@mui/material/Box';

interface CustomButtonProps extends ButtonProps {
  label: string;
  Icon: React.ComponentType;
}

const CustomButton: React.FC<CustomButtonProps> = ({ label, Icon, sx, ...props }) => {
  return (
    <Button
      {...props}
      role="button"
      aria-label={label}
      sx={{
        backgroundColor: '#1a1a1a',
        color: '#fff',
        padding: '25px 15px 15px 15px',
        borderRadius: '8px',
        width: '306px',
        height: '130px',
        fontSize: "24px",
        // minWidth: '100px', // added for responsiveness
        '&:hover': {
          backgroundColor: '#0e0e0e'
        },
        ...sx, // spread the user-provided styles here
      }}
    >
    <Box sx={{ display: 'flex', flexDirection: 'row', alignItems: 'center', justifyContent: 'flex-start', width: '100%' }}>
    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: '10px' }}>
    <Icon sx={{ backgroundColor: '#5D50C34D', borderRadius: '8px', padding: '2px' , height:"50px", width: "51px"}} />
      {label}
    </Box>
  </Box>

    </Button>
  );
};

export default CustomButton;
