import React, { useState } from "react";
import Papa from "papaparse";
import "./UploadCSV.css";

const UploadCSV = ({ onFileUpload }) => {
  const [csvData, setCsvData] = useState(null);
  const [isJsonVisible, setIsJsonVisible] = useState(false);

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (!file) return;

    if (!file.name.endsWith(".csv")) {
      alert("Please upload a valid CSV file.");
      return;
    }

    Papa.parse(file, {
      header: true,
      skipEmptyLines: true,
      complete: (result) => {
        if (!result.data || result.data.length === 0) {
          alert("CSV file is empty or improperly formatted.");
          return;
        }
        try {
          const jsonData = processUserAndTaskData(result.data);
          if (!jsonData.users.length || !jsonData.tasks.length) {
            alert("CSV file must contain both users and tasks.");
            return;
          }
          setCsvData(jsonData);
          onFileUpload(jsonData);
        } catch (error) {
          console.error("Error processing CSV:", error);
          alert("An error occurred while processing the CSV file. Please check formatting.");
        }
      },
      error: (error) => {
        console.error("CSV Parsing Error:", error);
        alert("Failed to read CSV file. Ensure it is properly formatted.");
      },
    });
  };

  const processUserAndTaskData = (data) => {
    let users = [];
    let tasks = [];
    let isTaskSection = false;

    data.forEach((row, index) => {
      if (!row["# Users"]) return; // Skip empty rows

      if (row["# Users"].trim() === "# Tasks") {
        isTaskSection = true;
        return;
      }

      try {
        if (!isTaskSection) {
          if (users.length === 0 && row["# Users"].toLowerCase().includes("user id")) return; // Skip header row
          users.push({
            id: row["# Users"].trim(),
            name: row.__parsed_extra?.[0]?.trim() || "Unnamed User",
            skills: row.__parsed_extra?.[1] ? row.__parsed_extra[1].split(";").map(skill => skill.trim()) : [],
            availableHours: parseInt(row.__parsed_extra?.[2]) || 0,
          });
        } else {
          if (tasks.length === 0 && row["# Users"].toLowerCase().includes("task id")) return; // Skip header row
          tasks.push({
            id: row["# Users"].trim(),
            name: row.__parsed_extra?.[0]?.trim() || "Untitled Task",
            requiredSkills: row.__parsed_extra?.[1] ? row.__parsed_extra[1].split(";").map(skill => skill.trim()) : [],
            estimatedHours: parseInt(row.__parsed_extra?.[2]) || 0,
          });
        }
      } catch (err) {
        console.warn("Skipping malformed row:", row);
      }
    });

    return { users, tasks };
  };

  return (
    <div className="upload-container">
      <h2>Upload CSV File</h2>
      <input type="file" accept=".csv" onChange={handleFileUpload} />

      {csvData && (
        <div className="data-preview">
          <h3>User List</h3>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Skills</th>
                <th>Available Hours</th>
              </tr>
            </thead>
            <tbody>
              {csvData.users.map((user, index) => (
                <tr key={index}>
                  <td>{user.id}</td>
                  <td>{user.name}</td>
                  <td>{user.skills.join(", ")}</td>
                  <td>{user.availableHours}</td>
                </tr>
              ))}
            </tbody>
          </table>

          <h3>Task List</h3>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Task Name</th>
                <th>Required Skills</th>
                <th>Estimated Hours</th>
              </tr>
            </thead>
            <tbody>
              {csvData.tasks.map((task, index) => (
                <tr key={index}>
                  <td>{task.id}</td>
                  <td>{task.name}</td>
                  <td>{task.requiredSkills.join(", ")}</td>
                  <td>{task.estimatedHours}</td>
                </tr>
              ))}
            </tbody>
          </table>

          <button onClick={() => setIsJsonVisible(!isJsonVisible)}>
            {isJsonVisible ? "Hide JSON Data" : "Show JSON Data"}
          </button>

          {isJsonVisible && (
            <pre className="json-preview">
              {JSON.stringify(csvData, null, 2)}
            </pre>
          )}
        </div>
      )}
    </div>
  );
};

export default UploadCSV;
