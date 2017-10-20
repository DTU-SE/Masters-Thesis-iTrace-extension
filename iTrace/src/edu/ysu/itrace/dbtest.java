package edu.ysu.itrace;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

import com.mysql.jdbc.Connection;

public class dbtest {

  public static void main(String[] args) {
    try {
      int sce_gaze_id;
      Class.forName("com.mysql.jdbc.Driver");   
      java.sql.Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/iTrace","root","1234");
      ResultSet rs = conn.createStatement().executeQuery("SELECT max(gaze_id) FROM gazes WHERE gaze_session_id='20171020t111536-0120+0200';");
      System.out.println("query done");
      rs.next();
      sce_gaze_id = rs.getInt("max(gaze_id)");
      System.out.println(sce_gaze_id);

      
    } catch (SQLException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    } catch (ClassNotFoundException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
    
    
  }
}
