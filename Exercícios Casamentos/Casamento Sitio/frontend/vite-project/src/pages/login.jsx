import { useState } from "react";

import {API} from "../services/api"

import "./login.css"

export default function Login({onLogin}) {
    const [emial,setEmail]= useState("")
    const [password, setPassword]= useState("")
        async function handleLogin(e) {
        e.preve
    }
            const token = res.data.token || res.data.access_token
            localStorage.setItem("token",token)
            onLogin(token)

           catch (error) (
            console.log(error.response?.data)
            alert("Erro no login")
        )
    
    return(
        <div className="login-container">
            <form onSubmit={handleLogin} className="login-form">
                
                <h1 className="login-title">Login</h1>
                
                <title>Sistema de convidados</title>
                
                <input 
                className="login-input"
                placeholder="email"  
                value={email} 
                onChange={(e) => setEmail(e.target.value)} />
                
                <input 
                className="login-input"
                placeholder="senha"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}/>
            
            <button className="login-button" type="submit">Entrar</button>
            
            </form>
        </div>
    )
}