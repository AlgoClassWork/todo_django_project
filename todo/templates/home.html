<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Список задач</title>
  <style>
    :root {
      --accent: #3b82f6;
      --accent-hover: #2563eb;
      --bg: #ffffff;
      --bg-secondary: #f9fafb;
      --text: #111827;
      --text-muted: #6b7280;
      --border: #e5e7eb;
      --success: #10b981;
      --warning: #f59e0b;
      --radius: 8px;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Inter', system-ui, sans-serif;
      background-color: var(--bg-secondary);
      color: var(--text);
      line-height: 1.6;
      padding: 20px;
    }

    .container {
      max-width: 700px;
      margin: 0 auto;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 30px 20px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
    }

    header {
      text-align: center;
      margin-bottom: 30px;
    }

    h1 {
      font-size: 2rem;
      font-weight: 600;
      margin-bottom: 10px;
    }

    form {
      display: flex;
      gap: 10px;
      margin-top: 20px;
    }

    input[type="text"] {
      flex: 1;
      padding: 12px 16px;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      font-size: 1rem;
      transition: border-color 0.2s;
    }

    input[type="text"]:focus {
      border-color: var(--accent);
      outline: none;
    }

    button {
      background: var(--accent);
      color: #fff;
      padding: 12px 20px;
      border: none;
      border-radius: var(--radius);
      cursor: pointer;
      font-weight: 500;
      transition: background 0.2s;
    }

    button:hover {
      background: var(--accent-hover);
    }

    .task-list {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }

    .task-card {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px;
      background: var(--bg-secondary);
      border-radius: var(--radius);
      transition: box-shadow 0.2s, transform 0.2s;
    }

    .task-card:hover {
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
      transform: translateY(-2px);
    }

    .task-info {
      flex: 1;
    }

    .task-title {
      font-size: 1.1rem;
      font-weight: 500;
    }

    .task-date {
      font-size: 0.85rem;
      color: var(--text-muted);
    }

    .status-badge {
      padding: 6px 12px;
      font-size: 0.8rem;
      border-radius: 999px;
      font-weight: 500;
      text-align: center;
      white-space: nowrap;
      transition: background 0.2s;
    }

    .completed .status-badge {
      background: var(--success);
      color: white;
    }

    .pending .status-badge {
      background: var(--warning);
      color: white;
    }

    .task-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-left: 20px;
    }

    .task-actions a {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 1.1rem;
      transition: color 0.2s;
    }

    .task-actions a:hover {
      color: var(--accent);
    }

    @media (max-width: 600px) {
      form {
        flex-direction: column;
      }

      button {
        width: 100%;
      }

      .task-card {
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
      }

      .task-actions {
        margin-left: 0;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>Мои задачи</h1>
      <form action="{% url 'add' %}" method="post">
        {% csrf_token %}
        <input type="text" name="title" placeholder="Новая задача">
        <button type="submit">Добавить</button>
      </form>
    </header>

    <div class="task-list">
      {% for task in tasks %}
        <div class="task-card {% if task.completed %}completed{% else %}pending{% endif %}">
          <div class="task-info">
            <div class="task-title">{{ task.title }}</div>
            <div class="task-date">Создано: {{ task.created_at|date:"d M Y" }}</div>
          </div>
          <div class="task-actions">
            <a class="status-badge" href="{% url 'complete' task.id %}">
              {% if task.completed %}Завершено{% else %}В процессе{% endif %}
            </a>
            <a href="{% url 'delete' task.id %}">❌</a>
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
</body>
</html>
