import React from 'react';
import { Navigate } from 'react-router-dom';

const Auth = (Component) => {
    return (props) => {
        const { isAuthenticated } = props;

        if (!isAuthenticated) {
            return <Navigate to="/blog" replace />;
        }

        return <Component {...props} />;
    };
};

export default Auth;