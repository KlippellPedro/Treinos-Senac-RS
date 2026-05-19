import { useNavigate } from "react-router-dom"

export default function Menu() {
  const navigate = useNavigate()

  return (
    <div style={{ display: "flex", gap: 10, padding: 10 }}>

      <button onClick={() => navigate("/dashboard")}>
        Dashboard
      </button>

      <button onClick={() => navigate("/guests")}>
        Convidados
      </button>

      

    </div>
  )
}