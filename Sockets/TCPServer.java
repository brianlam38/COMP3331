/*
 *
 * tcpServer from Kurose and Ross
 *
 * Usage: java TCPServer [server port]
 */

import java.io.*;
import java.net.*;

public class TCPServer {

	public static void main(String[] args)throws Exception {


		// see if we do not use default server port
		int serverPort = 6789; 
		/* change above port number this if required */
		
		if (args.length >= 1)
		    serverPort = Integer.parseInt(args[0]);
	    
		// create server socket
		ServerSocket welcomeSocket = new ServerSocket(serverPort);

		while (true){

		    // accept connection from connection queue
		    Socket connectionSocket = welcomeSocket.accept();
		    System.out.println("connection from " + connectionSocket);

		    // create read stream to get input
		    BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
		    String clientSentence;
		    clientSentence = inFromClient.readLine();

		    // process input
		    String capitalizedSentence;
		    capitalizedSentence = clientSentence.toUpperCase() + '\n';

		    // send reply
		    DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
		    outToClient.writeBytes(capitalizedSentence);

		} // end of while (true)

	} // end of main()

} // end of class TCPServer
