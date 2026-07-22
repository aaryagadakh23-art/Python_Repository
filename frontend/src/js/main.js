import { API_URL } from "./api.js";

const API = (API_URL | "http://127.0.0.1:8000");

const form = document.getElementById("studentForm");

const table = document.getElementById("studentTable");

loadStudents();

async function loadStudents(){

    const response = await fetch(`${API}/students`);

    const students = await response.json();

    table.innerHTML = "";

    students.forEach(student=>{

        table.innerHTML += `

        <tr>

            <td>${student.id}</td>

            <td>${student.name}</td>

            <td>${student.email}</td>

            <td>${student.age}</td>

            <td>

                <button
                    class="action-btn edit"
                    onclick="editStudent(${student.id})">

                    Edit

                </button>

                <button
                    class="action-btn delete"
                    onclick="deleteStudent(${student.id})">

                    Delete

                </button>

            </td>

        </tr>

        `;

    });

}

form.addEventListener("submit", async function(e){

    e.preventDefault();

    const id = document.getElementById("studentId").value;

    const student = {

        name:document.getElementById("name").value,

        email:document.getElementById("email").value,

        age:Number(document.getElementById("age").value)

    };

    if(id===""){

        await fetch(`${API}/students`,{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify(student)

        });

    }

    else{

        await fetch(`${API}/students/${id}`,{

            method:"PUT",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify(student)

        });

    }

    form.reset();

    document.getElementById("studentId").value="";

    loadStudents();

});

async function editStudent(id){

    const response = await fetch(`${API}/students/${id}`);

    const student = await response.json();

    document.getElementById("studentId").value = student.id;

    document.getElementById("name").value = student.name;

    document.getElementById("email").value = student.email;

    document.getElementById("age").value = student.age;

}

async function deleteStudent(id){

    if(!confirm("Delete Student?"))

        return;

    await fetch(`${API}/students/${id}`,{

        method:"DELETE"

    });

    loadStudents();

}