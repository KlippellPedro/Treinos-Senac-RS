import { useState,useEffect } from "react"

import Login from "./pages/login"

import Guest from "./pages/guest"

function App() {

  const [token, setToken]=useState(null)
  useEffect(() => {
    const savedToken=localStorage.getItem("token")
    if (savedToken){
      setToken(savedToken)
    }
  }, [])

  function handleLogin(jwt) {
    setToken(jwt)
  }

  function logout(){
    localStorage.removeItem("token")
    setToken(null)
  }

  return(
    <div>
      {!token ? (
        <Login onLogin={handleLogin} />
      ) : (
        <>
          <Guest>
        </>
      )}
    </div>
  )
}

export default App