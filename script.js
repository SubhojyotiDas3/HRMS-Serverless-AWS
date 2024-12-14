const API_BASE_URL =
  "https://<your-api-gateway-id>.execute-api.<region>.amazonaws.com/<stage>";

// Fetch all employees and populate the table
async function fetchEmployees() {
  const response = await fetch(`${API_BASE_URL}/employee`, { method: "GET" });
  const employees = await response.json();

  const tableBody = document.getElementById("employeeTableBody");
  tableBody.innerHTML = ""; // Clear previous entries

  employees.forEach((employee) => {
    const row = `<tr>
            <td>${employee.empId}</td>
            <td>${employee.empName}</td>
            <td>${employee.empDept}</td>
            <td>${employee.empEmail}</td>
        </tr>`;
    tableBody.innerHTML += row;
  });
}

// Search for an employee by name
async function searchEmployee() {
  const searchName = document.getElementById("searchName").value.toLowerCase();

  const response = await fetch(`${API_BASE_URL}/employee`, { method: "GET" });
  const employees = await response.json();

  const filteredEmployees = employees.filter((employee) =>
    employee.empName.toLowerCase().includes(searchName)
  );

  const tableBody = document.getElementById("employeeTableBody");
  tableBody.innerHTML = ""; // Clear previous entries

  filteredEmployees.forEach((employee) => {
    const row = `<tr>
            <td>${employee.empId}</td>
            <td>${employee.empName}</td>
            <td>${employee.empDept}</td>
            <td>${employee.empEmail}</td>
        </tr>`;
    tableBody.innerHTML += row;
  });
}
