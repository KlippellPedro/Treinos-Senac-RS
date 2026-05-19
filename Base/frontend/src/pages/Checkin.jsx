
import { useState } from "react"

import { API } from "../services/api"


import "./Checkin.css"

export default function Checkin() {


  const [search, setSearch] = useState("")


  const [guests, setGuests] = useState([])

 
  const [loading, setLoading] = useState(false)


  async function handleSearch() {

   
    if (!search) return

    setLoading(true)

    try {

    
      const res = await API.guest.get(
        `/guests?search=${search}`
      )

 
      setGuests(res.data)

    } catch (err) {

      console.log(err.response?.data)

      alert(
        err.response?.data?.error ||
        "Erro ao buscar convidados"
      )

    } finally {
      setLoading(false)
    }
  }


  async function handleCheckin(id_convidado) {

    try {

  
      await API.checkin.post("/checkin", {
        id_convidado,
        id_usuario: 1 
      })

     
      setGuests(prev =>
        prev.filter(
          g => g.id_convidado !== id_convidado
        )
      )

      alert("Check-in realizado com sucesso!")

    } catch (err) {

      alert(
        err.response?.data?.error ||
        "Erro no check-in"
      )
    }
  }

  return (
    <div className="checkin-container">


      <h1>Check-in de Convidados</h1>

  
      <div className="checkin-search">

        <input
          placeholder="Buscar por nome ou CPF"
          value={search}
          onChange={(e) => setSearch(e.target.value)}

         
          onKeyDown={(e) =>
            e.key === "Enter" && handleSearch()
          }
        />

        <button onClick={handleSearch}>
          Buscar
        </button>

      </div>


      {loading && <p>Buscando convidados...</p>}


      <div className="checkin-list">

        {guests.map((g) => (
          <div
            key={g.id_convidado}
            className="checkin-card"
          >

 
            <div>
              <strong>
                {g.nome} {g.sobrenome}
              </strong>

              <p>CPF: {g.cpf}</p>
            </div>

            {/* BOTÃO CHECK-IN */}
            <button
              onClick={() =>
                handleCheckin(g.id_convidado)
              }
            >
              Fazer Check-in
            </button>

          </div>
        ))}

      </div>

    </div>
  )
}