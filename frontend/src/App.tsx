import { useEffect, useState } from 'react'
import { api } from './services/api'

interface Task {
  id: number;
  title: string;
  priority: number;
  status: string;
}

function App() {
  const [tasks, setTasks] = useState<Task[]>([])

  useEffect(() => {
    // 1. Le decimos explícitamente a 'api.get' que espere un arreglo de tareas: <Task[]>
    api.get<Task[]>('/tasks/')
      .then((response: { data: Task[] }) => {
        setTasks(response.data)
      })
      // 2. Le decimos explícitamente que el error puede ser de cualquier tipo (any)
      .catch((error: any) => {
        console.error("Error conectando con el backend:", error)
      })
  }, [])

  return (
    <div className="min-h-screen bg-slate-100 p-8 font-sans">
      <div className="max-w-2xl mx-auto bg-white rounded-xl shadow-lg p-6 border border-slate-200">
        
        <header className="mb-6 border-b pb-4">
          <h1 className="text-3xl font-bold text-slate-800">Mi Asistente Universitario</h1>
          <p className="text-slate-500 mt-1">Tus tareas sincronizadas desde SQLite</p>
        </header>

        <ul className="space-y-3">
          {tasks.length === 0 ? (
            <p className="text-slate-500 italic text-center py-4">No hay tareas guardadas. ¡Crea una en el backend!</p>
          ) : (
            tasks.map(task => (
              <li key={task.id} className="p-4 border border-slate-200 rounded-lg flex justify-between items-center hover:bg-slate-50 transition-colors">
                <span className="font-medium text-slate-700">{task.title}</span>
                <span className="text-xs font-semibold px-3 py-1 bg-indigo-100 text-indigo-700 rounded-full capitalize">
                  {task.status.replace('_', ' ')}
                </span>
              </li>
            ))
          )}
        </ul>

      </div>
    </div>
  )
}

export default App