// Importa hook useState para controlar estado dos inputs
import { useState } from "react"

// Importa hook de navegação do React Router
import { useNavigate } from "react-router-dom"

// Importa API centralizada (Axios configurado)
import { API } from "../services/api"

// Importa arquivo de estilo CSS do login
import "./Login.css"

// Componente de login que recebe função onLogin como props
export default function Login({ onLogin }) {

  // Hook para navegar entre páginas
  const navigate = useNavigate()

  // Estado para armazenar o email digitado
  const [email, setEmail] = useState("")

  // Estado para armazenar a senha digitada
  const [password, setPassword] = useState("")

  // Função executada ao enviar o formulário
  async function handleLogin(e) {

    // Evita recarregar página
    e.preventDefault()

    try {

      // Requisição POST para login
      const res = await API.auth.post("/login", {

        email,
        senha: password,
      })

      // Captura token
      const token = res.data.token || res.data.access_token

      // Salva no localStorage
      localStorage.setItem("token", token)

      // Atualiza estado global
      onLogin(token)

      
      navigate("/guests")

    } catch (err) {

      console.log(err.response?.data)

      alert("Erro no login")
    }
  }

  return (
    <div className="login-container">

      <form onSubmit={handleLogin} className="login-form">

        <h1 className="login-title">Login</h1>

        <input
          className="login-input"
          placeholder="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          className="login-input"
          placeholder="senha"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button className="login-button" type="submit">
          Entrar
        </button>

      </form>

    </div>
  )
}