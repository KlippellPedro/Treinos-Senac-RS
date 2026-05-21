// Importa o Axios para fazer requisições HTTP
import axios from "axios"

// Função que cria uma instância configurada da API
const createAPI = (baseURL) => {

  // Cria um cliente Axios com uma URL base definida
  const api = axios.create({ baseURL })

  // Interceptor: executa antes de TODA requisição
  api.interceptors.request.use((config) => {

    // Pega o token salvo no navegador
    const token = localStorage.getItem("token")

    // Se existir token
    if (token) {
      // Adiciona o token no header da requisição (JWT padrão)
      config.headers.Authorization = `Bearer ${token}`
    }

    // Retorna a configuração modificada da requisição
    return config
  })

  // Retorna a instância configurada do Axios
  return api
}

// Exporta várias APIs separadas por microserviço
export const API = {

  // Serviço de autenticação (login, registro, etc.)
  auth: createAPI("http://localhost:5001"),

  // Serviço de convidados (CRUD de guests)
  guest: createAPI("http://localhost:5002"),

  // Serviço de check-in (entrada de convidados)
  checkin: createAPI("http://localhost:5004"),

  // Serviço de usuários (admin, perfil, etc.)
  user: createAPI("http://localhost:5003"),
}