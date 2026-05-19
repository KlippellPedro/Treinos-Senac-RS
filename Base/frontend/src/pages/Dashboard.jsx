import { useEffect, useState } from "react"
import { API } from "../services/api"
import "./Dashboard.css"

export default function Dashboard() {

  const [guests, setGuests] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadData()
  }, [])

  async function loadData() {
    try {
      const res = await API.guest.get("/guests?event_id=1")
      setGuests(res.data)
    } catch (err) {
      console.log(err.response?.data)
      alert("Erro ao carregar dashboard")
    } finally {
      setLoading(false)
    }
  }


  const total = guests.length
  const confirmados = guests.filter(g => g.status === "confirmado").length
  const pendentes = guests.filter(g => g.status === "pendente").length

  return (
    <div className="dashboard-container">

      <h1>Dashboard Wedding Pass</h1>

      {loading && <p>Carregando dados...</p>}

      {!loading && (
        <div className="dashboard-cards">

          <div className="card total">
            <h2>Total</h2>
            <p>{total}</p>
          </div>

          <div className="card confirmados">
            <h2>Confirmados</h2>
            <p>{confirmados}</p>
          </div>

          <div className="card pendentes">
            <h2>Pendentes</h2>
            <p>{pendentes}</p>
          </div>

        </div>
      )}

    </div>
  )
}