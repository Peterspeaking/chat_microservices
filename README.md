# Chat Microservices

A chat microservices project utilizing WebSockets

1. **User Service**: Manages user information.
2. **Chat Service**: Facilitates real-time communication using WebSockets and interacts with the User service.

#### User Service

1. **Create a User:**

   ```bash
   curl -X POST http://localhost:5002/users -H "Content-Type: application/json" -d '{"id": 1, "name": "John Doe"}'
   ```

2. **List Users:**

   ```bash
   curl -X GET http://localhost:5002/users
   ```

3. **Get User by ID:**

   ```bash
   curl -X GET http://localhost:5002/users/1
   ```

#### Chat Service

1. **Connect to WebSocket Via Postman:**

   - Create a new WebSocket request in Postman.
   - Enter the WebSocket URL: `ws://localhost:6789`.
   - Click "Connect".

2. **Send a Message:**

   - In the WebSocket message input field, enter:
     ```json
     {
       "user_id": 1,
       "content": "Hello, everyone!"
     }
     ```
   - Click "Send".

3. **Receive Messages:**
   - Messages will be displayed in the Postman WebSocket response log.
