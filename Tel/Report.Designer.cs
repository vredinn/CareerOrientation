
namespace Tel
{
    partial class Report
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.button1 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.Name_user = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Nomber_phone = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.prof_name = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Items.AddRange(new object[] {
            "1-Строительство",
            "2-Информационные системы и технологии",
            "3-Металлургия",
            "4-Прикладная информатика",
            "5-Теплоэнергетика и теплотехника",
            "6-Электроэнергетика и электротехника",
            "7-Технологические машины и оборудование",
            "8-Конструкторско-технологическое обеспечение машиностроения",
            "9-Экономика",
            "10-Химическая технология",
            "11-Боеприпасы и взрыватели",
            "12-Транспортные средства специального назначения",
            "13-Мехатроника и робототехника",
            "Все"});
            this.comboBox1.Location = new System.Drawing.Point(127, 19);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(503, 24);
            this.comboBox1.TabIndex = 0;
            this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // dataGridView1
            // 
            this.dataGridView1.AllowUserToAddRows = false;
            this.dataGridView1.AllowUserToDeleteRows = false;
            this.dataGridView1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.Name_user,
            this.Nomber_phone,
            this.prof_name});
            this.dataGridView1.Location = new System.Drawing.Point(0, 62);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.ReadOnly = true;
            this.dataGridView1.RowHeadersWidth = 51;
            this.dataGridView1.RowTemplate.Height = 24;
            this.dataGridView1.Size = new System.Drawing.Size(800, 388);
            this.dataGridView1.TabIndex = 1;
            this.dataGridView1.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView1_CellContentClick);
            // 
            // button1
            // 
            this.button1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.button1.Location = new System.Drawing.Point(636, 8);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(152, 44);
            this.button1.TabIndex = 2;
            this.button1.Text = "Экспортировать в Excel";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click_1);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(13, 22);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(108, 16);
            this.label1.TabIndex = 3;
            this.label1.Text = "Специальность";
            // 
            // Name_user
            // 
            this.Name_user.DataPropertyName = "user_name";
            this.Name_user.HeaderText = "Имя пользователя";
            this.Name_user.MinimumWidth = 6;
            this.Name_user.Name = "Name_user";
            this.Name_user.ReadOnly = true;
            this.Name_user.Width = 125;
            // 
            // Nomber_phone
            // 
            this.Nomber_phone.DataPropertyName = "user_phone";
            this.Nomber_phone.HeaderText = "Номер телефона";
            this.Nomber_phone.MinimumWidth = 6;
            this.Nomber_phone.Name = "Nomber_phone";
            this.Nomber_phone.ReadOnly = true;
            this.Nomber_phone.Width = 125;
            // 
            // prof_name
            // 
            this.prof_name.DataPropertyName = "prof_name";
            this.prof_name.HeaderText = "Специальность";
            this.prof_name.MinimumWidth = 6;
            this.prof_name.Name = "prof_name";
            this.prof_name.ReadOnly = true;
            this.prof_name.Width = 125;
            // 
            // Report
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.comboBox1);
            this.Name = "Report";
            this.Text = "Профориентатор - Просмотр пользователей";
            this.Shown += new System.EventHandler(this.Report_Shown);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.DataGridViewTextBoxColumn Name_user;
        private System.Windows.Forms.DataGridViewTextBoxColumn Nomber_phone;
        private System.Windows.Forms.DataGridViewTextBoxColumn prof_name;
    }
}

