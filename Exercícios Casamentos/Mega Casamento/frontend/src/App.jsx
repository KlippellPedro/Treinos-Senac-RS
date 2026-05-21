import { BrowserRouter, Routes, Route, Navigate, useLocation } from "react-router-dom"
import { useState } from "react"

import Login from "./pages/Login"
import Guests from "./pages/Guests"
import GuestForm from "./pages/GuestForm"
import Checkin from "./pages/Checkin"
import Dashboard from "./pages/Dashboard"
import Menu from "./pages/Menu"

function AppContent() {

  const location = useLocation()

  const [token, setToken] = useState(() => {
    return localStorage.getItem("token")
  })

  function handleLogin(jwt) {
    localStorage.setItem("token", jwt)
    setToken(jwt)
  }

  function logout() {
    localStorage.removeItem("token")
    setToken(null)
  }

  if (token === undefined) {
    return null
  }

  return (
    <>
    
      {token && location.pathname !== "/login" && location.pathname !== "/checkin" && <Menu />}

      <Routes>

     
        <Route
          path="/login"
          element={<Login onLogin={handleLogin} />}
        />

   
        <Route
          path="/"
          element={
            <Navigate
              to={token ? "/dashboard" : "/login"}
              replace
            />
          }
        />

   
        <Route
          path="/dashboard"
          element={
            token ? (
              <Dashboard />
            ) : (
              <Navigate to="/login" replace />
            )
          }
        />

     
        <Route
          path="/guests"
          element={
            token ? (
              <Guests onLogout={logout} />
            ) : (
              <Navigate to="/login" replace />
            )
          }
        />

        <Route
          path="/guests/new"
          element={
            token ? (
              <GuestForm />
            ) : (
              <Navigate to="/login" replace />
            )
          }
        />

    
        <Route
          path="/guests/edit/:id"
          element={
            token ? (
              <GuestForm />
            ) : (
              <Navigate to="/login" replace />
            )
          }
        />

     
        <Route
          path="/checkin"
          element={
            token ? (
              <Checkin />
            ) : (
              <Navigate to="/login" replace />
            )
          }
        />

      </Routes>
    </>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <AppContent />
    </BrowserRouter>
  )
}