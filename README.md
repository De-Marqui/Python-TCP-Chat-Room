# Simple TCP Thread Chat Room
<p>
  <sub>Terminal Chat Room Simulation using connection-oriented protocol (TCP Protocol) with Threading tosimultaneously receive and send messages through it's application</sub>
  <br><br>
  <sup> It was used localhost as server HOST just for simplify local simulations </sup>
  <br>
  <pre>
    <code>  HOST = 'localhost'
      PORT = 32014
      serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      serverSocket.bind((HOST,PORT))
      serverSocket.listen()</code></pre>
</p>

> <sup>Program Running</sup>
> <img src = "https://cdn.discordapp.com/attachments/820795354823786508/955241698273931274/unknown.png">
>> <sup>After a Client disconnection</sup>
>> <img src = "https://cdn.discordapp.com/attachments/820795354823786508/955241953392484372/unknown.png">
