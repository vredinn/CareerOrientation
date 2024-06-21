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
    public partial class Report : Form
    {
        public Report()
        {
            InitializeComponent();
        }

        public void displayReport()
        {
            connection.display("SELECT user_name,user_phone,telegram_id,prof_name FROM users JOIN professions ON users.profession = professions.prof_id", dataGridView1);
        }

        private void Report_Shown(object sender, EventArgs e)
        {
            displayReport();
            foreach (DataGridViewColumn column in dataGridView1.Columns)
            {
                column.SortMode = DataGridViewColumnSortMode.NotSortable;
            }
        }

        public DataTable queryReturnData(string query, DataTable dataTable)
        {
            MySqlConnection myCon = connection.GetConnection();

            MySqlDataAdapter SDA = new MySqlDataAdapter(query, myCon);
            SDA.SelectCommand.ExecuteNonQuery();

            SDA.Fill(dataTable);
            return dataTable;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (comboBox1.SelectedIndex)
            {

                case 0:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Строительство%'";

                    break;
                case 1:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Информационные системы и технологии%'";

                    break;
                case 2:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Металлургия%'";

                    break;

                case 3:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Прикладная информатика%'";

                    break;
                case 4:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Теплоэнергетика и теплотехника%'";

                    break;
                case 5:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Электроэнергетика и электротехника%'";

                    break;

                case 6:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Технологические машины и оборудование%'";

                    break;
                case 7:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Конструкторско-технологическое обеспечение машиностроения%'";

                    break;
                case 8:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Экономика%'";

                    break;

                case 9:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Химическая технология%'";

                    break;
                case 10:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Боеприпасы и взрыватели%'";

                    break;
                case 11:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Транспортные средства специального назначения%'";

                    break;
                case 12:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%Мехатроника и робототехника%'";

                    break;
                case 13:

                    (dataGridView1.DataSource as DataTable).DefaultView.RowFilter = $"prof_name LIKE '%%'";

                    break;


            }
        }

        private void ExportToExcel(DataTable dataTable)
        {
            if (dataTable.Rows.Count > 0)
            {
                Microsoft.Office.Interop.Excel.Application excel = new Microsoft.Office.Interop.Excel.Application();
                excel.Application.Workbooks.Add(Type.Missing);

                for (int i = 1; i < dataTable.Columns.Count + 1; i++)
                {
                    excel.Cells[1, i] = dataTable.Columns[i - 1].ColumnName;
                }

                for (int i = 0; i < dataTable.Rows.Count; i++)
                {
                    for (int j = 0; j < dataTable.Columns.Count; j++)
                    {
                        excel.Cells[i + 2, j + 1] = dataTable.Rows[i][j].ToString();
                    }
                }

                excel.Columns.AutoFit();
                excel.Visible = true;
            }
            else
            {
                MessageBox.Show("No data to export!");
            }
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            var query = "SELECT user_name,user_phone,telegram_id,prof_name FROM users JOIN professions ON users.profession = professions.prof_id";
            if (comboBox1.SelectedIndex != 13)
            {
                query = query + " WHERE users.profession = " + (comboBox1.SelectedIndex + 1);
                MessageBox.Show(query);
            }
            

            var table = new DataTable();

            queryReturnData(query, table);

            ExportToExcel(table);
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
