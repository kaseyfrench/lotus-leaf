import AppBar from 'material-ui/AppBar';
import PropTypes from 'prop-types';
import React from 'react';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';

class PrimaryHeader extends React.Component {
  render() {
    return (
      <AppBar position="static">
        <Toolbar>
          <Typography type="title" color="inherit">{this.props.title}</Typography>
          {this.props.children}
        </Toolbar>
      </AppBar>
    );
  }
}

PrimaryHeader.propTypes = {
  title: PropTypes.string.isRequired
};

export default PrimaryHeader;
