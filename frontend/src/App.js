import React, { useState } from "react";
import UploadCSV from "./components/UploadCSV";
import TaskAllocator from "./components/TaskAllocator";
import "./App.css";

function App() {
  const [csvData, setCsvData] = useState(null);

  return (
    <div className="app-container">
      <h1>AI Task Allocation</h1>
      <UploadCSV onFileUpload={setCsvData} />
      {csvData && <TaskAllocator data={csvData} />}
    </div>
  );
}

export default App;
