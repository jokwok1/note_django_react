import Form from "../components/Form"
import { useLocation } from 'react-router-dom';


const Login = () => {
  const location = useLocation();
  const message = location.state?.message;

  return (
    <>
    {message && <div className="alert alert-success">{message}</div>}
    <Form route="/api/token/" method="login" />
    </>
  )
}

export default Login