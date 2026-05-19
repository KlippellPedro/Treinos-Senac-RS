import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Guests from "./pages/Guests";
import GuestForm from "./pages/GuestForm";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        {/* HOME -> lista de convidados */}
        <Route
          path="/"
          element={<Navigate to="/guests" />}
        />

        {/* LISTA DE CONVIDADOS */}
        <Route
          path="/guests"
          element={<Guests />}
        />

        {/* CRIAR CONVIDADO */}
        <Route
          path="/guests/new"
          element={<GuestForm />}
        />

        {/* EDITAR CONVIDADO */}
        <Route
          path="/guests/edit/:id"
          element={<GuestForm />}
        />

        {/* fallback */}
        <Route
          path="*"
          element={<Navigate to="/guests" />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;