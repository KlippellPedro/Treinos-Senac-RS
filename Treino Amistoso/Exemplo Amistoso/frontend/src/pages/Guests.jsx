import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { API } from "../services/api";

import "./Guests.css";

export default function Guests() {

  const navigate = useNavigate();
  const [guests, setGuests] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadGuests();
  }, []);

  async function loadGuests() {
    try {
      const res = await API.guest.get("/guests");
      setGuests(res.data);
    } catch (err) {
      console.log(err);
    } finally {
      setLoading(false);
    }
  }

  async function handleDelete(id) {
    if (!confirm("Excluir convidado?")) return;

    try {
      await API.guest.delete(`/guests/${id}`);
      setGuests(prev => prev.filter(g => g.id_convidado !== id));
    } catch (err) {
      console.log(err);
    }
  }

  return (
    <div className="guests-container">

      <h1 className="guests-title">
        Convidados ({guests.length})
      </h1>

      <div className="top-actions">
        <button
          className="new-guest-button"
          onClick={() => navigate("/guests/new")}
        >
          Novo Convidado
        </button>
      </div>

      {loading && <p>Carregando...</p>}

      <div className="guests-list">

        {guests.map((g) => (
          <div className="guest-card" key={g.id_convidado}>

            <div className="guest-name">
              {g.nome}
            </div>

            <p className="guest-text">{g.email}</p>

            <button onClick={() =>
              navigate(`/guests/edit/${g.id_convidado}`)
            }>
              Editar
            </button>

            <button onClick={() => handleDelete(g.id_convidado)}>
              Excluir
            </button>

          </div>
        ))}

      </div>

    </div>
  );
}