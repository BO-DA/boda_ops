import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

public class SocketIOServer {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("######## Argument is Null ########");
            return ;
        }
        
        int port = Integer.parseInt(args[0]);

        // 읽을 파일의 경로 및 파일명 지정
        String filePath = "/Users/jinjae/Code/Jinjae/Project/Hackerthon/boda_ops/socket-server/res.txt";
        String line = "";

        try (ServerSocket serverSocket = new ServerSocket(port)) {
 
            System.out.println("Server is listening on port " + port);
 
            while (true) {
                Socket socket = serverSocket.accept();

                System.out.println("[ "+socket.getInetAddress()+" ] client connected");
                OutputStream output = socket.getOutputStream();

                try {
                    // FileReader와 BufferedReader를 사용하여 파일 읽기
                    FileReader fileReader = new FileReader(filePath);
                    BufferedReader bufferedReader = new BufferedReader(fileReader);

                    // 파일의 끝까지 한 줄씩 읽어오기
                    line = bufferedReader.readLine();

                    // 파일 닫기
                    bufferedReader.close();
                } catch (IOException e) {
                    // 예외 처리
                    e.printStackTrace();
                }

                PrintWriter writer = new PrintWriter(output, true);
                System.out.println(line);
                writer.println(line);

                socket.close();
            }
 
        } catch (IOException ex) {
            System.out.println("Server exception: " + ex.getMessage());
            ex.printStackTrace();
        }

    }

}
