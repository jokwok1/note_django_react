// Protected Route act as a wrapper for a protected route, so anything wrapped 
// inside requires authentication

import {Navigate} from "react-router-dom"
import {jwtDecode} from "jwt-decode"
import api from "../api"
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants"
import { useState, useEffect } from "react"

function ProtectedRoute({children}) {
    const [isAuthorized, setIsAuthorized] = useState(null);

    useEffect(() => {
        auth().catch(() => setIsAuthorized(false));
    }, []);

    const refreshToken = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);
        try {
            // get new refresh token
            const res = await api.post("/api/token/refresh/", {refresh : refreshToken,});
            if (res.status === 200) {
                //success status
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                // res.data.access refers to the new access token returned 
                //by the server after a successful refresh token reques
                setIsAuthorized(true);
            } else {
                setIsAuthorized(false);
            }
        } catch (error) {
            console.log(error);
            setIsAuthorized(false);
        }
    }

    const auth = async () => {
        // check if you have token
        const token = localStorage.getItem(ACCESS_TOKEN)
        if (!token) {
            setIsAuthorized(false);
            return
        }
        // decode token and checked if expired
        const decoded = jwtDecode(token);
        const tokenExpiration = decoded.exp;
        const now = Date.now() / 1000;

        if (tokenExpiration < now ) {
            //toke already expired
            await refreshToken();
        } else {
            setIsAuthorized(true); // successfully authorized since not expired
        }
    }

    if (isAuthorized === null) {
        return <div>Loading...</div>
    }

    return isAuthorized ? children : <Navigate to="/login/" />

    
}

export default ProtectedRoute

