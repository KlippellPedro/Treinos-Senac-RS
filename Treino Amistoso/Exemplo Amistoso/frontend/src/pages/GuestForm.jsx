import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { API } from "../services/api";

import "./GuestForm.css";

export default function GuestForm() {
  const navigate = useNavigate();
  const { id } = useParams();

  const [form, setForm] = useState({
    id_evento: 1,
    nome: "",
    sobrenome: "",
    cpf: "",
    telefone: "",
    email: "",
    numero_mesa: "",
    tipo_convidado: "Familia"
  });

  useEffect(() => {
    if (id) loadGuest();
  }, [id]);

  async function loadGuest() {
    try {
      const res = await API.guest.get(`/guests/${id}`);
      setForm(res.data);
    } catch (err) {
      console.log(err);
    }
  }


  function formatCPF(value) {
    value = value.replace(/\D/g, "");
    value = value.replace(/(\d{3})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
    return value;
  }

  function handleCPFChange(e) {
    setForm({ ...form, cpf: formatCPF(e.target.value) });
  }

 
  function formatPhone(value) {
    value = value.replace(/\D/g, "");

   
    value = value.replace(/(\d{2})(\d)/, "($1) $2");
    value = value.replace(/(\d{5})(\d)/, "$1-$2");

    return value;
  }

  function handlePhoneChange(e) {
    setForm({ ...form, telefone: formatPhone(e.target.value) });
  }


  function validateForm() {
    const errors = [];

    if (!form.nome) errors.push("Nome");
    if (!form.sobrenome) errors.push("Sobrenome");
    if (!form.cpf) errors.push("CPF");
    if (!form.email) errors.push("Email");
    if (!form.telefone) errors.push("Telefone");
    if (!form.numero_mesa) errors.push("Mesa");
    if (!form.tipo_convidado) errors.push("Tipo de convidado");

    if (errors.length > 0) {
      alert("Preencha os campos obrigatórios:\n\n" + errors.join("\n"));
      return false;
    }

    return true;
  }

  async function handleSubmit() {
    try {
      if (!validateForm()) return;

      if (id) {
        await API.guest.put(`/guests/${id}`, form);
      } else {
        await API.guest.post("/guests", form);
      }

      navigate("/guests");

    } catch (err) {
      console.log(err);
      alert("Erro ao salvar convidado");
    }
  }

  return (
    <div className="guest-form">

      <label>Nome:</label>
      <input
        value={form.nome}
        onChange={(e) => setForm({ ...form, nome: e.target.value })}
      />

      <label>Sobrenome:</label>
      <input
        value={form.sobrenome}
        onChange={(e) => setForm({ ...form, sobrenome: e.target.value })}
      />

      <label>CPF:</label>
      <input
        value={form.cpf}
        onChange={handleCPFChange}
        maxLength={14}
        placeholder="000.000.000-00"
      />

      <label>Email:</label>
      <input
        value={form.email}
        onChange={(e) => setForm({ ...form, email: e.target.value })}
      />

      <label>Telefone:</label>
      <input
        value={form.telefone}
        onChange={handlePhoneChange}
        maxLength={15}
        placeholder="(00) 00000-0000"
      />

      <label>Mesa:</label>
      <input
        type="number"
        value={form.numero_mesa}
        onChange={(e) =>
          setForm({ ...form, numero_mesa: e.target.value })
        }
      />

      <label>Tipo de Convidado:</label>
      <select
        value={form.tipo_convidado}
        onChange={(e) =>
          setForm({ ...form, tipo_convidado: e.target.value })
        }
      >
        <option value="Familia">Família</option>
        <option value="Amigos">Amigos</option>
      </select>

      <button onClick={handleSubmit}>
        {id ? "Atualizar" : "Criar"}
      </button>

    </div>
  );
}