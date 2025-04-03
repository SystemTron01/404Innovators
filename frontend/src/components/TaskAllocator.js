import React from "react";
import "./TaskAllocator.css";

const TaskAllocator = ({ data }) => {
  if (!data || !Array.isArray(data.tasks) || !Array.isArray(data.users)) {
    console.error("Invalid task allocation data:", data);
    return <p style={{ color: "red" }}>Error loading task allocations.</p>;
  }

  const allocateTasks = (users, tasks) => {
    return tasks
      .filter((task) => task.id.toLowerCase() !== "task id") // Skip header row
      .map((task) => {
        if (!task.requiredSkills || !Array.isArray(task.requiredSkills)) {
          console.warn("Skipping task due to missing required skills:", task);
          return { task: task.name || "Unnamed Task", assignedTo: "Unassigned" };
        }

        const assignedUser =
          users.find((user) =>
            task.requiredSkills.some((skill) => user.skills.includes(skill))
          ) || { name: "Unassigned" };

        return { task: task.name || "Unnamed Task", assignedTo: assignedUser.name };
      });
  };

  const taskAssignments = allocateTasks(data.users, data.tasks);

  return (
    <div className="task-allocator">
      <h2>Task Allocations</h2>
      <table>
        <thead>
          <tr>
            <th>Task</th>
            <th>Assigned To</th>
          </tr>
        </thead>
        <tbody>
          {taskAssignments.map((assignment, index) => (
            <tr key={index}>
              <td>{assignment.task}</td>
              <td>{assignment.assignedTo}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TaskAllocator;
