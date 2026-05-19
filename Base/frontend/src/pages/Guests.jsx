import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"
import { API } from "../services/api"
import "./Guests.css"

export default function Guests() {

  const navigate = useNavigate()


  const [guests, setGuests] = useState([])
  const [loading, setLoading] = useState(true)
  const [search, setSearch] = useState("")


  useEffect(() => {
    loadGuests()
  }, [])

  async function loadGuests() {
    try {
      const res = await API.guest.get("/guests?event_id=1")
      setGuests(res.data)
    } catch (err) {
      console.log(err.response?.data)
    } finally {
      setLoading(false)
    }
  }


  async function handleCheckin(id_convidado) {
    try {

      const token = localStorage.getItem("token")

      await API.checkin.post(
        `/checkin/${id_convidado}`,
        {},
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      )

      setGuests(prev =>
        prev.map(g =>
          g.id_convidado === id_convidado
            ? { ...g, status: "confirmado" }
            : g
        )
      )

    } catch (err) {
      console.log(err.response?.data)
      alert(err.response?.data?.error || "Erro no check-in")
    }
  }


  async function handleDelete(id) {

    if (!confirm("Excluir convidado?")) return

    try {
      await API.guest.delete(`/guests/${id}`)

      setGuests(prev =>
        prev.filter(g => g.id_convidado !== id)
      )

    } catch (err) {
      console.log(err.response?.data)
      alert("Erro ao deletar")
    }
  }


  const filteredGuests = guests.filter(g => {
    const t = search.toLowerCase()

    return (
      g.nome?.toLowerCase().includes(t) ||
      g.sobrenome?.toLowerCase().includes(t) ||
      g.cpf?.includes(t)
    )
  })


  const sortedGuests = [...filteredGuests].sort((a, b) => {
    return (a.status === "confirmado") - (b.status === "confirmado")
  })


  return (
    <div className="guests-container">

      <h1 className="guests-title">
        Convidados ({guests.length})
      </h1>

      <button
        className="new-guest-button"
        onClick={() => navigate("/guests/new")}
      >
        Novo Convidado
      </button>

   
      <div className="search-bar">

        <div className="search-input-wrapper">

          <span className="search-icon"></span>

          <input
            placeholder="Buscar por nome, sobrenome ou CPF..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />

          {search && (
            <button
              className="clear-btn"
              onClick={() => setSearch("")}
            >
              ✕
            </button>
          )}

        </div>

      </div>

     
      {loading && <p>Carregando...</p>}

     
      <div className="guests-list">

        {sortedGuests.length === 0 && !loading && (
          <p style={{ textAlign: "center" }}>
            Nenhum convidado encontrado
          </p>
        )}

        {sortedGuests.map((g) => {

          const isChecked = g.status === "confirmado"

          return (
            <div key={g.id_convidado} className="guest-card">

              <div className="guest-name">
                {g.nome} {g.sobrenome}
              </div>

              <p>CPF: {g.cpf}</p>
              <p>Email: {g.email}</p>

              <p>
                Status: {" "}
                {isChecked ? "Confirmado" : "Pendente"}
              </p>

              <button
                onClick={() =>
                  navigate(`/guests/edit/${g.id_convidado}`)
                }
              >
                Editar
              </button>

              <button onClick={() => handleDelete(g.id_convidado)}>
                Excluir
              </button>

              <button
                onClick={() => handleCheckin(g.id_convidado)}
                disabled={isChecked}
                style={{
                  backgroundColor: isChecked ? "#999" : "#28a745",
                  color: "white",
                  marginTop: "5px",
                  cursor: isChecked ? "not-allowed" : "pointer"
                }}
              >
                {isChecked ? "Já fez check-in" : "Check-in"}
              </button>

            </div>
          )
        })}

      </div>

     
      <div className="logout-container">
        <button
          className="logout-button"
          onClick={() => {
            localStorage.removeItem("token")
            window.location.reload()
          }}
        >
          Sair
        </button>
      </div>

    </div>
  )
}