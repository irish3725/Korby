package ca.stt;

import java.io.*;
import java.net.*;

public class TCPClient {

    String ip;
    int port;
    // message to send
    public String message;
    // message received from server
    public String reply;
    // boolean for if we have a message to send
    public boolean send = false;
    // boolean for if we need to continue to poll
    public boolean poll = true;

    // client variables
    private BufferedReader inFromUser;
    private Socket clientSocket;
    private DataOutputStream outToServer;
    private BufferedReader inFromServer;

    public TCPClient(String ip, int port) {
        System.out.println("entered tcp client constructor");
        this.ip = ip;
        this.port = port;
        try {
            // client vairables
            // string input
            this.inFromUser = new BufferedReader(new InputStreamReader(System.in));
            // initiate client socket
            this.clientSocket = new Socket(this.ip, this.port);
            // for sending data to server
            this.outToServer = new DataOutputStream(clientSocket.getOutputStream());
            // for receiving reply from server
            this.inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            System.out.println("connected to host: " + this.ip + " on port: " + this.port);
        } catch (IOException e) {
            System.out.println("\n\nunable to connect to server\n\n");
            e.printStackTrace();
        }

    }

    public void sendMessage(String message) {
        this.message = message;
        this.send = true;
        System.out.println("running send message");

        System.out.println("Sending message: " + this.message);
        // send message to other server

        try {
            this.outToServer.writeBytes(this.message + '\n');
            // get reply from server
            this.reply = this.inFromServer.readLine();
            System.out.println("FROM SERVER: " + this.reply);
            this.send = false;
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void stopPolling() throws IOException {
        this.poll = false;
        this.clientSocket.close();
    }

    public void run(){
    }

//    public void start(){
//        System.out.println("Starting tcp client thread");
//        if(t == null){
//            t = new Thread(this, "client");
//            t.start();
//        }
//    }
}
