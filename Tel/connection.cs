using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;
using System.Data.SqlClient;

namespace Tel
{
    class connection
    {
        public static MySqlConnection GetConnection()
        {
            string sql = "datasource=141.8.192.82;port=3306;username=a0947295_admin;password=killerbob;database=a0947295_carrierordb";
            MySqlConnection con = new MySqlConnection(sql);
            try
            {
                con.Open();
            }
            catch (MySqlException ex)
            {
                MessageBox.Show("MySQL Connection! \n" + ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            return con;
        }

        public static void display(string qrt, DataGridView dgv)
        {
            string sql = qrt;

            MySqlConnection con = GetConnection();

            MySqlCommand com = new MySqlCommand(sql, con);

            MySqlDataAdapter adp = new MySqlDataAdapter(com);

            DataTable dt = new DataTable();

            adp.Fill(dt);

            dgv.DataSource = dt;

            con.Close();

        }
    }
}
