import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font
import psycopg2
from psycopg2 import Error
import sys
from datetime import datetime


class ModernButton:
    """Custom modern button class with hover effects"""

    def __init__(self, parent, text, command, bg_color, hover_color, text_color='white', **kwargs):
        self.bg_color = bg_color
        self.hover_color = hover_color

        self.button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg_color,
            fg=text_color,
            relief='flat',
            bd=0,
            cursor='hand2',
            font=('Segoe UI', 12, 'bold'),
            **kwargs
        )

        # Bind hover effects
        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.button.configure(bg=self.hover_color)

    def on_leave(self, event):
        self.button.configure(bg=self.bg_color)

    def pack(self, **kwargs):
        self.button.pack(**kwargs)

    def grid(self, **kwargs):
        self.button.grid(**kwargs)


class SportClubGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sport Club Management System")
        self.root.geometry("1400x900")

        # Modern color scheme
        self.colors = {
            'primary': '#2C3E50',  # Dark blue-gray
            'secondary': '#34495E',  # Lighter blue-gray
            'accent': '#3498DB',  # Blue
            'success': '#27AE60',  # Green
            'warning': '#F39C12',  # Orange
            'danger': '#E74C3C',  # Red
            'light': '#ECF0F1',  # Light gray
            'dark': '#2C3E50',  # Dark
            'background': '#F8F9FA',  # Very light gray
            'card': '#FFFFFF',  # White
            'gradient_start': '#667eea',  # Purple-blue
            'gradient_end': '#764ba2'  # Purple
        }

        # Set modern styling
        self.setup_modern_style()

        # Database connection parameters
        self.db_params = {
            'host': 'localhost',
            'database': 'stage4',
            'port': '5432',
            'user': 'cradia8155',
            'password': 'cradia2004'
        }

        self.connection = None
        self.cursor = None

        # Initialize database connection
        self.connect_to_database()

        # Create main interface
        self.create_modern_interface()

    def setup_modern_style(self):
        """Setup modern styling for the application"""
        self.root.configure(bg=self.colors['background'])

        # Configure modern ttk style
        style = ttk.Style()
        style.theme_use('clam')

        # Configure treeview style
        style.configure("Modern.Treeview",
                        background=self.colors['card'],
                        foreground=self.colors['primary'],
                        rowheight=35,
                        fieldbackground=self.colors['card'],
                        borderwidth=0,
                        relief="flat")

        style.configure("Modern.Treeview.Heading",
                        background=self.colors['primary'],
                        foreground='white',
                        relief="flat",
                        borderwidth=1)

        # Configure frame style
        style.configure("Card.TFrame",
                        background=self.colors['card'],
                        relief="flat",
                        borderwidth=1)

    def connect_to_database(self):
        """Connect to PostgreSQL database"""
        try:
            self.connection = psycopg2.connect(**self.db_params)
            self.cursor = self.connection.cursor()
            print("Database connection successful")
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {e}")
            sys.exit(1)

    def create_modern_interface(self):
        """Create modern main interface"""
        # Create gradient background effect using frames
        self.create_gradient_background()

        # Main container with card effect
        main_container = tk.Frame(self.root, bg=self.colors['card'], relief='flat', bd=0)
        main_container.place(relx=0.5, rely=0.5, anchor='center', width=1200, height=760)

        # Add shadow effect
        shadow_frame = tk.Frame(self.root, bg=self.colors['card'], relief='flat', bd=0)
        shadow_frame.place(relx=0.5, rely=0.505, anchor='center', width=1200, height=760)
        main_container.lift()

        # Header section
        self.create_modern_header(main_container)

        # Navigation cards
        self.create_navigation_cards(main_container)

        # Footer
        self.create_footer(main_container)

    def create_gradient_background(self):
        """Create gradient background effect"""
        # Create multiple frames for gradient effect
        for i in range(100):
            color_ratio = i / 100
            # Simple gradient simulation
            r1, g1, b1 = int(self.colors['gradient_start'][1:3], 16), int(self.colors['gradient_start'][3:5], 16), int(
                self.colors['gradient_start'][5:7], 16)
            r2, g2, b2 = int(self.colors['gradient_end'][1:3], 16), int(self.colors['gradient_end'][3:5], 16), int(
                self.colors['gradient_end'][5:7], 16)

            r = int(r1 + (r2 - r1) * color_ratio)
            g = int(g1 + (g2 - g1) * color_ratio)
            b = int(b1 + (b2 - b1) * color_ratio)

            color = f"#{r:02x}{g:02x}{b:02x}"

            gradient_frame = tk.Frame(self.root, bg=color, height=9)
            gradient_frame.place(x=0, y=i * 9, relwidth=1)

    def create_modern_header(self, parent):
        """Create modern header section"""
        header_frame = tk.Frame(parent, bg=self.colors['card'], height=120)
        header_frame.pack(fill=tk.X, padx=30, pady=(30, 20))
        header_frame.pack_propagate(False)

        # App icon (using text for now)
        icon_frame = tk.Frame(header_frame, bg=self.colors['accent'], width=80, height=80)
        icon_frame.place(x=0, y=20)
        icon_frame.pack_propagate(False)

        icon_label = tk.Label(icon_frame, text="💪", font=('Segoe UI Emoji', 32),
                              bg=self.colors['accent'], fg='white')
        icon_label.place(relx=0.5, rely=0.5, anchor='center')

        # Title and subtitle
        title_frame = tk.Frame(header_frame, bg=self.colors['card'])
        title_frame.place(x=100, y=10, relwidth=0.7, height=100)

        title_label = tk.Label(title_frame, text="Sport Club Management",
                               font=('Segoe UI', 28, 'bold'),
                               bg=self.colors['card'], fg=self.colors['primary'])
        title_label.pack(anchor='w')

        subtitle_label = tk.Label(title_frame, text="Manage members, courses, and trainers with ease",
                                  font=('Segoe UI', 14),
                                  bg=self.colors['card'], fg=self.colors['secondary'])
        subtitle_label.pack(anchor='w', pady=(5, 0))

        # Status indicator
        status_frame = tk.Frame(header_frame, bg=self.colors['card'])
        status_frame.place(relx=1, x=-150, y=20, width=140, height=60, anchor='ne')

        status_dot = tk.Frame(status_frame, bg=self.colors['success'], width=12, height=12)
        status_dot.place(x=0, y=5)

        status_label = tk.Label(status_frame, text="Database Connected",
                                font=('Segoe UI', 9),
                                bg=self.colors['card'], fg=self.colors['success'])
        status_label.place(x=20, y=2)

    def create_navigation_cards(self, parent):
        """Create modern navigation cards"""
        cards_frame = tk.Frame(parent, bg=self.colors['card'])
        cards_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        # Card data with icons, colors, and descriptions
        cards_data = [
            ("👥", "Member Management", "Add, edit, and manage club members",
             self.colors['accent'], "#2980B9", self.open_member_management),
            ("📚", "Class Management", "Organize and schedule Classs",
             self.colors['success'], "#229954", self.open_Class_management),
            ("🏃", "Trainer Management", "Manage trainer profiles and schedules",
             self.colors['danger'], "#CB4335", self.open_trainer_management),
            ("📊", "Analytics & Reports", "View insights and generate reports",
             self.colors['warning'], "#D68910", self.open_analytics),
            ("⚙️", "Database Functions", "Execute database procedures",
             "#9B59B6", "#8E44AD", self.open_functions),
            ("🏋️", "Registers For Classes", "Register a Member For Classes",
             "#95A5A6", "#7F8C8D", self.exit_application)
        ]

        # Create grid of cards
        for i, (icon, title, description, color, hover_color, command) in enumerate(cards_data):
            row = i // 3
            col = i % 3

            self.create_navigation_card(cards_frame, icon, title, description,
                                        color, hover_color, command, row, col)

    def create_navigation_card(self, parent, icon, title, description, color, hover_color, command, row, col):
        """Create individual navigation card"""
        card_frame = tk.Frame(parent, bg=color, relief='flat', bd=0, cursor='hand2')
        card_frame.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')

        # Configure grid weights
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(col, weight=1)

        # Card content
        content_frame = tk.Frame(card_frame, bg=color)
        content_frame.pack(expand=True, fill='both', padx=25, pady=25)

        # Icon
        icon_label = tk.Label(content_frame, text=icon, font=('Segoe UI Emoji', 40),
                              bg=color, fg='white')
        icon_label.pack(pady=(10, 15))

        # Title
        title_label = tk.Label(content_frame, text=title, font=('Segoe UI', 16, 'bold'),
                               bg=color, fg='white')
        title_label.pack()

        # Description
        desc_label = tk.Label(content_frame, text=description, font=('Segoe UI', 11),
                              bg=color, fg='white', wraplength=200)
        desc_label.pack(pady=(8, 15))

        # Hover effects
        def on_enter(event):
            card_frame.configure(bg=hover_color)
            content_frame.configure(bg=hover_color)
            icon_label.configure(bg=hover_color)
            title_label.configure(bg=hover_color)
            desc_label.configure(bg=hover_color)

        def on_leave(event):
            card_frame.configure(bg=color)
            content_frame.configure(bg=color)
            icon_label.configure(bg=color)
            title_label.configure(bg=color)
            desc_label.configure(bg=color)

        def on_click(event):
            command()

        # Bind events to all components
        for widget in [card_frame, content_frame, icon_label, title_label, desc_label]:
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Button-1>", on_click)

    def create_footer(self, parent):
        """Create modern footer"""
        footer_frame = tk.Frame(parent, bg=self.colors['light'], height=50)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)

        footer_label = tk.Label(footer_frame,
                                text="© 2024 Sport Club Management System | Modern Interface",
                                font=('Segoe UI', 10),
                                bg=self.colors['light'], fg=self.colors['secondary'])
        footer_label.place(relx=0.5, rely=0.5, anchor='center')

    def open_member_management(self):
        """Open member management window"""
        MemberManagementWindow(self)

    def open_Class_management(self):
        """Open Class management window"""
        ClassManagementWindow(self)

    def open_trainer_management(self):
        """Open trainer management window"""
        TrainerManagementWindow(self)

    def open_analytics(self):
        """Open analytics window"""
        AnalyticsWindow(self)

    def open_functions(self):
        """Open database functions window"""
        FunctionsWindow(self)


    def exit_application(self):
        RegistrationManagementWindow(self)

    # def exit_application(self):
    #     RegistrationManagementWindow
    #     """Exit the application with confirmation"""
    #     if messagebox.askyesno("Exit Confirmation",
    #                            "Are you sure you want to exit the application?",
    #                            icon='question'):
    #         if self.connection:
    #             self.connection.close()
    #         self.root.destroy()

    def run(self):
        """Start the GUI"""
        self.root.mainloop()


class MemberManagementWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent.root)
        self.window.title("Member Management")
        self.window.geometry("1200x800")
        self.window.configure(bg=parent.colors['background'])

        # Make window modal
        self.window.transient(parent.root)
        self.window.grab_set()

        self.create_modern_interface()
        self.refresh_members()

    def create_modern_interface(self):
        """Create modern member management interface"""
        # Header
        header_frame = tk.Frame(self.window, bg=self.parent.colors['primary'], height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        header_content = tk.Frame(header_frame, bg=self.parent.colors['primary'])
        header_content.pack(expand=True, fill='both', padx=30)

        icon_label = tk.Label(header_content, text="👥", font=('Segoe UI Emoji', 24),
                              bg=self.parent.colors['primary'], fg='white')
        icon_label.pack(side=tk.LEFT, pady=25)

        title_label = tk.Label(header_content, text="Member Management",
                               font=('Segoe UI', 24, 'bold'),
                               bg=self.parent.colors['primary'], fg='white')
        title_label.pack(side=tk.LEFT, padx=(15, 0), pady=25)

        # Action buttons frame
        buttons_frame = tk.Frame(self.window, bg=self.parent.colors['background'], height=80)
        buttons_frame.pack(fill=tk.X, padx=30, pady=(20, 0))
        buttons_frame.pack_propagate(False)

        # Modern action buttons
        btn_data = [
            ("+ Add Member", self.add_member, self.parent.colors['success'], "#229954"),
            ("✏️ Edit Member", self.edit_member, self.parent.colors['accent'], "#2980B9"),
            ("🗑️ Delete Member", self.delete_member, self.parent.colors['danger'], "#CB4335"),
            ("🔄 Refresh", self.refresh_members, self.parent.colors['secondary'], "#34495E")
        ]

        for text, command, color, hover_color in btn_data:
            btn = ModernButton(buttons_frame, text, command, color, hover_color,
                               width=15, height=2)
            btn.pack(side=tk.LEFT, padx=(0, 15), pady=20)

        # Data table frame with card styling
        table_frame = tk.Frame(self.window, bg=self.parent.colors['card'], relief='flat', bd=1)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(10, 30))

        # Treeview with modern styling
        self.tree = ttk.Treeview(table_frame,
                                 columns=('ID', 'Name','Gender', 'Birth Date', 'Type', 'Registration', 'Expiration'),
                                 show='headings', height=15,
                                 style="Modern.Treeview")

        # Configure columns
        columns_config = [
            ('ID', 70, 'ID'),
            ('Name', 200, 'Member Name'),
            ('Gender', 80, 'Gender'),
            ('Birth Date', 120, 'Birth Date'),
            ('Type', 150, 'Membership Type'),
            ('Registration', 140, 'Registration Date'),
            ('Expiration', 140, 'Expiration Date')
        ]

        for col_id, width, heading in columns_config:
            self.tree.heading(col_id, text=heading)
            self.tree.column(col_id, width=width, anchor='center')

        # Scrollbars
        v_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)

        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack everything
        self.tree.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        v_scrollbar.grid(row=0, column=1, sticky='ns', pady=20)
        h_scrollbar.grid(row=1, column=0, sticky='ew', padx=20)

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

    def refresh_members(self):
        """Updated refresh method to properly handle expiration date"""
        try:
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Query members with all fields including expiration date
            query = """
            SELECT m.person_id, p.person_name, p.gender, p.birth_date, 
                   m.membership_type, m.registrationdate, m.expirationdate
            FROM Member m
            JOIN Person p ON m.person_id = p.person_id
            ORDER BY m.person_id
            """
            self.parent.cursor.execute(query)
            members = self.parent.cursor.fetchall()

            # Insert into treeview with alternating colors
            for i, member in enumerate(members):
                # Format dates for display
                formatted_member = list(member)
                for j in [3, 5, 6]:  # birth_date, registration_date, expiration_date indices
                    if formatted_member[j]:
                        formatted_member[j] = str(formatted_member[j])
                    else:
                        formatted_member[j] = 'N/A'

                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                self.tree.insert('', 'end', values=formatted_member, tags=(tag,))

            # Configure row colors
            self.tree.tag_configure('evenrow', background='#F8F9FA')
            self.tree.tag_configure('oddrow', background='#FFFFFF')

        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh members: {e}")

    def add_member(self):
        """Add new member"""
        MemberFormWindow(self, "Add New Member")

    def edit_member(self):
        """Edit selected member"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a member to edit")
            return

        item = self.tree.item(selection[0])
        member_data = item['values']
        print("Member data:", member_data)
        MemberFormWindow(self, "Edit Member", member_data)

    def delete_member(self):
        """Delete selected member with confirmation"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a member to delete")
            return

        item = self.tree.item(selection[0])
        member_id = item['values'][0]
        member_name = item['values'][1]

        if messagebox.askyesno("Confirm Deletion",
                               f"Are you sure you want to delete member:\n{member_name} (ID: {member_id})?",
                               icon='warning'):
            try:
                # Delete with proper foreign key handling
                self.parent.cursor.execute("DELETE FROM registers_for WHERE person_id = %s", (member_id,))
                self.parent.cursor.execute("DELETE FROM Member WHERE person_id = %s", (member_id,))
                self.parent.cursor.execute("DELETE FROM Person WHERE person_id = %s", (member_id,))

                self.parent.connection.commit()
                messagebox.showinfo("Success", f"Member {member_name} deleted successfully!")
                self.refresh_members()

            except Exception as e:
                self.parent.connection.rollback()
                messagebox.showerror("Error", f"Failed to delete member: {e}")




#===================================== MemberFormWindow ==================================================

class MemberFormWindow:
    def __init__(self, parent, title, member_data=None):
        self.parent = parent
        self.member_data = member_data
        self.window = tk.Toplevel(parent.window)
        self.window.title(title)
        self.window.geometry("500x750")
        self.window.configure(bg=parent.parent.colors['background'])

        # Make window modal
        self.window.transient(parent.window)
        self.window.grab_set()

        # Center the window
        self.window.geometry("+%d+%d" % (parent.window.winfo_rootx() + 350,
                                         parent.window.winfo_rooty() + 100))

        self.create_modern_form()


        if member_data:
            self.populate_form()

    def create_modern_form(self):
        """Create modern member form"""
        # Header
        header_frame = tk.Frame(self.window, bg=self.parent.parent.colors['primary'], height=70)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        title_label = tk.Label(header_frame, text="Member Information",
                               font=('Segoe UI', 20, 'bold'),
                               bg=self.parent.parent.colors['primary'], fg='white')
        title_label.pack(expand=True)

        # Form container
        form_container = tk.Frame(self.window, bg=self.parent.parent.colors['card'])
        form_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        # Form fields
        fields_config = [
            ("Full Name", "name", "entry"),
            ("Gender", "gender", "combo", None, ['M', 'F']),
            ("Birth Date", "birth_date", "entry", "Format: YYYY-MM-DD"),
            ("Membership Type", "membership_type", "combo", None, ['Premium', 'Basic', 'Standart']),
            ("Registration Date", "reg_date", "entry", "Format: YYYY-MM-DD"),
            ("Expiration Date", "exp_date", "entry", "Format: YYYY-MM-DD")
        ]

        self.entries = {}

        for i, field_config in enumerate(fields_config):
            field_name = field_config[0]
            field_key = field_config[1]
            field_type = field_config[2]
            field_hint = field_config[3] if len(field_config) > 3 else None
            field_values = field_config[4] if len(field_config) > 4 else None

            # Field container
            field_frame = tk.Frame(form_container, bg=self.parent.parent.colors['card'])
            field_frame.pack(fill=tk.X, pady=(0, 20))

            # Label
            label = tk.Label(field_frame, text=field_name,
                             font=('Segoe UI', 12, 'bold'),
                             bg=self.parent.parent.colors['card'],
                             fg=self.parent.parent.colors['primary'])
            label.pack(anchor=tk.W)

            # Hint
            if field_hint:
                hint_label = tk.Label(field_frame, text=field_hint,
                                      font=('Segoe UI', 9),
                                      bg=self.parent.parent.colors['card'],
                                      fg=self.parent.parent.colors['secondary'])
                hint_label.pack(anchor=tk.W)

            # Input field
            if field_type == "combo":
                self.entries[field_key] = ttk.Combobox(
                    field_frame, values=field_values,
                    font=('Segoe UI', 11), height=12
                )
            else:
                self.entries[field_key] = tk.Entry(
                    field_frame, font=('Segoe UI', 11),
                    relief='flat', bd=5,
                    bg=self.parent.parent.colors['light'],
                    fg=self.parent.parent.colors['primary']
                )

            self.entries[field_key].pack(fill=tk.X, pady=(6, 0))

        # Buttons frame
        buttons_frame = tk.Frame(form_container, bg=self.parent.parent.colors['card'], height=80)
        buttons_frame.pack(fill=tk.X, pady=(30, 0))
        #buttons_frame.pack_propagate(False)

        # Action buttons
        save_btn = ModernButton(buttons_frame, "💾 Save Member", self.save_member,
                                self.parent.parent.colors['success'], "#229954",
                                width=15, height=2)
        save_btn.pack(side=tk.RIGHT, padx=(10, 0))

        cancel_btn = ModernButton(buttons_frame, "❌ Cancel", self.window.destroy,
                                  self.parent.parent.colors['secondary'], "#34495E",
                                  width=15, height=2)
        cancel_btn.pack(side=tk.RIGHT, pady=10)
        print("שדות קיימים:", self.entries.keys())

    def populate_form(self):
        """Populate form with existing member data"""
        if self.member_data:
            print("Member data:", self.member_data)
            self.entries['name'].insert(0, self.member_data[1])
            self.entries['gender'].set(self.member_data[2])  # הוספת gender
            self.entries['birth_date'].insert(0, str(self.member_data[3]))
            self.entries['membership_type'].set(self.member_data[4])
            self.entries['reg_date'].insert(0, str(self.member_data[5]))
            exp = self.member_data[6]
            if exp:
                self.entries['exp_date'].insert(0, str(exp))
            else:
                self.entries['exp_date'].insert(0, "")

    def save_member(self):
        """Save member data with validation"""
        try:
            # Get and validate form data
            name = self.entries['name'].get().strip()
            gender = self.entries['gender'].get().strip()
            birth_date = self.entries['birth_date'].get().strip()
            membership_type = self.entries['membership_type'].get().strip()
            reg_date = self.entries['reg_date'].get().strip()
            exp_date = self.entries['exp_date'].get().strip()

            # Validation
            if not all([name, gender, birth_date, membership_type, reg_date, exp_date]):
                messagebox.showerror("Validation Error", "All fields are required!")
                return

            # Database operations
            if self.member_data:  # Edit existing member
                member_id = self.member_data[0]

                self.parent.parent.cursor.execute(
                    "UPDATE Person SET person_name = %s, birth_date = %s WHERE person_id = %s",
                    (name, birth_date, member_id)
                )

                self.parent.parent.cursor.execute(
                    "UPDATE Member SET membership_type = %s, registrationdate = %s, expirationdate = %s WHERE person_id = %s",
                    (membership_type, reg_date, exp_date, member_id)
                )

                success_msg = f"Member {name} updated successfully!"
            else:  # Add new member
                # שלב 1: קבלי את ה-id הכי גבוה
                self.parent.parent.cursor.execute("SELECT COALESCE(MAX(person_id), 0)  FROM Person")
                person_id = self.parent.parent.cursor.fetchone()[0] + 1

                # שלב 2: הכניסי את האדם עם המזהה
                self.parent.parent.cursor.execute(
                    "INSERT INTO Person (person_id, person_name, gender, birth_date) VALUES (%s, %s, %s, %s)",
                    (person_id, name, gender, birth_date)
                )

                # שלב 3: הכניסי את החברות
                self.parent.parent.cursor.execute(
                    "INSERT INTO Member (person_id, membership_type, registrationdate, expirationdate) VALUES (%s, %s, %s, %s)",
                    (person_id, membership_type, reg_date, exp_date)
                )
                success_msg = f"Member {name} added successfully!"

            self.parent.parent.connection.commit()
            messagebox.showinfo("Success", success_msg)
            self.parent.refresh_members()
            self.window.destroy()

        except Exception as e:
            self.parent.parent.connection.rollback()
            messagebox.showerror("Database Error", f"Failed to save member: {e}")


# ===================================== ClassManagementWindow ==================================

# Modern design pattern for class management windows...
class ClassManagementWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent.root)
        self.window.title("Class Management")
        self.window.geometry("1200x700")
        self.window.configure(bg=parent.colors['background'])

        self.window.transient(parent.root)
        self.window.grab_set()

        self.create_modern_interface()
        self.refresh_classes()

    def create_modern_interface(self):
        """Create modern class management interface"""
        # Header
        header_frame = tk.Frame(self.window, bg=self.parent.colors['success'], height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        header_content = tk.Frame(header_frame, bg=self.parent.colors['success'])
        header_content.pack(expand=True, fill='both', padx=30)

        icon_label = tk.Label(header_content, text="🏋️", font=('Segoe UI Emoji', 24),
                              bg=self.parent.colors['success'], fg='white')
        icon_label.pack(side=tk.LEFT, pady=25)

        title_label = tk.Label(header_content, text="Class Management",
                               font=('Segoe UI', 24, 'bold'),
                               bg=self.parent.colors['success'], fg='white')
        title_label.pack(side=tk.LEFT, padx=(15, 0), pady=25)

        # Action buttons frame
        buttons_frame = tk.Frame(self.window, bg=self.parent.colors['background'], height=80)
        buttons_frame.pack(fill=tk.X, padx=30, pady=(20, 0))
        buttons_frame.pack_propagate(False)

        # Modern action buttons
        btn_data = [
            ("+ Add Class", self.add_class, self.parent.colors['success'], "#229954"),
            ("✏️ Edit Class", self.edit_class, self.parent.colors['accent'], "#2980B9"),
            ("🗑️ Delete Class", self.delete_class, self.parent.colors['danger'], "#CB4335"),
            ("🔄 Refresh", self.refresh_classes, self.parent.colors['secondary'], "#34495E")
        ]

        for text, command, color, hover_color in btn_data:
            btn = ModernButton(buttons_frame, text, command, color, hover_color,
                               width=15, height=2)
            btn.pack(side=tk.LEFT, padx=(0, 15), pady=20)

        # Data table frame with card styling
        table_frame = tk.Frame(self.window, bg=self.parent.colors['card'], relief='flat', bd=1)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(10, 30))

        # Treeview with modern styling
        self.tree = ttk.Treeview(table_frame,
                                 columns=('Gender', 'Trainer', 'Room', 'Course', 'Timeslot', 'Registrants'),
                                 show='headings', height=15,
                                 style="Modern.Treeview")

        # Configure columns
        columns_config = [
            ('Gender', 80, 'Gender'),
            ('Trainer', 200, 'Trainer Name'),
            ('Room', 150, 'Room Name'),
            ('Course', 200, 'Course Name'),
            ('Timeslot', 200, 'Time Schedule'),
            ('Registrants', 100, 'Registrants')
        ]

        for col_id, width, heading in columns_config:
            self.tree.heading(col_id, text=heading)
            self.tree.column(col_id, width=width, anchor='center')

        # Scrollbars
        v_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)

        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack everything
        self.tree.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        v_scrollbar.grid(row=0, column=1, sticky='ns', pady=20)
        h_scrollbar.grid(row=1, column=0, sticky='ew', padx=20)

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

    def refresh_classes(self):
        """Refresh the classes list"""
        try:
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Query classes with all related information
            query = """
            SELECT 
                cl.gender,
                p.person_name AS trainer_name,
                r.room_name,
                co.course_name,
                CONCAT(ts.day, ' ', ts.start_time, '-', ts.end_time) AS timeslot,
                cl.registrants,
                cl.timeslot_id,
                cl.room_id,
                cl.person_id,
                cl.course_id
            FROM class cl
            LEFT JOIN person p ON cl.person_id = p.person_id
            LEFT JOIN room r ON cl.room_id = r.room_id
            LEFT JOIN course co ON cl.course_id = co.course_id
            LEFT JOIN timeslot ts ON cl.timeslot_id = ts.timeslot_id
            ORDER BY ts.day, ts.start_time;
            """
            self.parent.cursor.execute(query)
            classes = self.parent.cursor.fetchall()

            # Insert into treeview with alternating colors
            for i, class_data in enumerate(classes):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                # Display only the first 6 columns, store all data
                display_values = class_data[:6]
                self.tree.insert('', 'end', values=display_values, tags=(tag,))

            # Configure row colors
            self.tree.tag_configure('evenrow', background='#F8F9FA')
            self.tree.tag_configure('oddrow', background='#FFFFFF')

        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh classes: {e}")

    def add_class(self):
        """Add new class"""
        ClassFormWindow(self, "Add New Class")

    def edit_class(self):
        """Edit selected class"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a class to edit")
            return

        # Get the full class data for editing
        try:
            item = self.tree.item(selection[0])
            display_values = item['values']

            # We need to get the full data including IDs for editing
            query = """
            SELECT 
                cl.gender,
                cl.person_id,
                cl.room_id,
                cl.course_id,
                cl.timeslot_id,
                cl.registrants,
                p.person_name,
                r.room_name,
                co.course_name,
                CONCAT(ts.day, ' ', ts.start_time, '-', ts.end_time) AS timeslot
            FROM class cl
            LEFT JOIN person p ON cl.person_id = p.person_id
            LEFT JOIN room r ON cl.room_id = r.room_id
            LEFT JOIN course co ON cl.course_id = co.course_id
            LEFT JOIN timeslot ts ON cl.timeslot_id = ts.timeslot_id
            WHERE cl.timeslot_id = %s AND cl.room_id = %s
            """

            # Find the class by matching displayed data
            self.parent.cursor.execute("""
            SELECT 
                cl.gender,
                cl.person_id,
                cl.room_id,
                cl.course_id,
                cl.timeslot_id,
                cl.registrants
            FROM class cl
            LEFT JOIN person p ON cl.person_id = p.person_id
            LEFT JOIN room r ON cl.room_id = r.room_id
            LEFT JOIN course co ON cl.course_id = co.course_id
            LEFT JOIN timeslot ts ON cl.timeslot_id = ts.timeslot_id
            WHERE p.person_name = %s AND r.room_name = %s AND co.course_name = %s
            """, (display_values[1], display_values[2], display_values[3]))

            class_data = self.parent.cursor.fetchone()
            if class_data:
                ClassFormWindow(self, "Edit Class", class_data)
            else:
                messagebox.showerror("Error", "Could not find class data for editing")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to get class data: {e}")

    def delete_class(self):
        """Delete selected class with confirmation"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a class to delete")
            return

        item = self.tree.item(selection[0])
        display_values = item['values']
        trainer_name = display_values[1]
        room_name = display_values[2]
        course_name = display_values[3]
        timeslot = display_values[4]

        if messagebox.askyesno("Confirm Deletion",
                               f"Are you sure you want to delete class:\n"
                               f"Course: {course_name}\n"
                               f"Trainer: {trainer_name}\n"
                               f"Room: {room_name}\n"
                               f"Time: {timeslot}?",
                               icon='warning'):
            try:
                # Find and delete the class
                self.parent.cursor.execute("""
                DELETE FROM class cl
                USING person p, room r, course co, timeslot ts
                WHERE cl.person_id = p.person_id 
                  AND cl.room_id = r.room_id 
                  AND cl.course_id = co.course_id
                  AND cl.timeslot_id = ts.timeslot_id
                  AND p.person_name = %s 
                  AND r.room_name = %s 
                  AND co.course_name = %s
                """, (trainer_name, room_name, course_name))

                self.parent.connection.commit()
                messagebox.showinfo("Success", "Class deleted successfully!")
                self.refresh_classes()

            except Exception as e:
                self.parent.connection.rollback()
                messagebox.showerror("Error", f"Failed to delete class: {e}")


class ClassFormWindow:
    def __init__(self, parent, title, class_data=None):
        self.parent = parent
        self.class_data = class_data
        self.window = tk.Toplevel(parent.window)
        self.window.title(title)
        self.window.geometry("500x750")
        self.window.configure(bg=parent.parent.colors['background'])

        # Make window modal
        self.window.transient(parent.window)
        self.window.grab_set()

        # Center the window
        self.window.geometry("+%d+%d" % (parent.window.winfo_rootx() + 350,
                                         parent.window.winfo_rooty() + 100))

        self.create_modern_form()

        if class_data:
            self.populate_form()

    def create_modern_form(self):
        """Create modern class form"""
        # Header
        header_frame = tk.Frame(self.window, bg=self.parent.parent.colors['success'], height=70)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        title_label = tk.Label(header_frame, text="Class Information",
                               font=('Segoe UI', 20, 'bold'),
                               bg=self.parent.parent.colors['success'], fg='white')
        title_label.pack(expand=True)

        # Form container
        form_container = tk.Frame(self.window, bg=self.parent.parent.colors['card'])
        form_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        # Get data for dropdowns
        self.get_form_data()

        # Form fields
        self.entries = {}

        # Gender Selection
        self.create_form_field(form_container, "Gender", "gender", "combo",
                               values=["M", "F"], hint="M=Male, F=Female")

        # Trainer Selection
        self.create_form_field(form_container, "Trainer", "trainer", "combo",
                               values=self.trainer_options)

        # Room Selection
        self.create_form_field(form_container, "Room", "room", "combo",
                               values=self.room_options)

        # Course Selection
        self.create_form_field(form_container, "Course", "course", "combo",
                               values=self.course_options)

        # Timeslot Selection
        self.create_form_field(form_container, "Timeslot", "timeslot", "combo",
                               values=self.timeslot_options)

        # Registrants
        self.create_form_field(form_container, "Number of Registrants", "registrants", "entry",
                               "Current number of registered participants")

        # Buttons frame
        buttons_frame = tk.Frame(form_container, bg=self.parent.parent.colors['card'])
        buttons_frame.pack(fill=tk.X, pady=(30, 0))

        # Action buttons
        save_btn = ModernButton(buttons_frame, "💾 Save Class", self.save_class,
                                self.parent.parent.colors['success'], "#229954",
                                width=15, height=2)
        save_btn.pack(side=tk.RIGHT, padx=(10, 0))

        cancel_btn = ModernButton(buttons_frame, "❌ Cancel", self.window.destroy,
                                  self.parent.parent.colors['secondary'], "#34495E",
                                  width=15, height=2)
        cancel_btn.pack(side=tk.RIGHT)

    def create_form_field(self, parent, label_text, field_key, field_type, hint=None, values=None):
        """Create a form field with consistent styling"""
        # Field container
        field_frame = tk.Frame(parent, bg=self.parent.parent.colors['card'])
        field_frame.pack(fill=tk.X, pady=(0, 20))

        # Label
        label = tk.Label(field_frame, text=label_text,
                         font=('Segoe UI', 12, 'bold'),
                         bg=self.parent.parent.colors['card'],
                         fg=self.parent.parent.colors['primary'])
        label.pack(anchor=tk.W)

        # Hint
        if hint:
            hint_label = tk.Label(field_frame, text=hint,
                                  font=('Segoe UI', 9),
                                  bg=self.parent.parent.colors['card'],
                                  fg=self.parent.parent.colors['secondary'])
            hint_label.pack(anchor=tk.W)

        # Input field
        if field_type == "combo":
            self.entries[field_key] = ttk.Combobox(
                field_frame, values=values if values else [],
                font=('Segoe UI', 11), height=12, state="readonly"
            )
        else:
            self.entries[field_key] = tk.Entry(
                field_frame, font=('Segoe UI', 11),
                relief='flat', bd=5,
                bg=self.parent.parent.colors['light'],
                fg=self.parent.parent.colors['primary']
            )

        self.entries[field_key].pack(fill=tk.X, pady=(5, 0))

    def get_form_data(self):
        """Get data for form dropdowns"""
        try:
            # Get trainers
            self.parent.parent.cursor.execute("""
                SELECT t.person_id, p.person_name 
                FROM trainer t 
                JOIN person p ON t.person_id = p.person_id 
                ORDER BY p.person_name
            """)
            trainers = self.parent.parent.cursor.fetchall()
            self.trainer_dict = {f"{name} (ID: {id})": id for id, name in trainers}
            self.trainer_options = list(self.trainer_dict.keys())

            # Get rooms
            self.parent.parent.cursor.execute("""
                SELECT room_id, room_name 
                FROM room 
                ORDER BY room_name
            """)
            rooms = self.parent.parent.cursor.fetchall()
            self.room_dict = {f"{name} (ID: {id})": id for id, name in rooms}
            self.room_options = list(self.room_dict.keys())

            # Get courses
            self.parent.parent.cursor.execute("""
                SELECT course_id, course_name 
                FROM course 
                ORDER BY course_name
            """)
            courses = self.parent.parent.cursor.fetchall()
            self.course_dict = {f"{name} (ID: {id})": id for id, name in courses}
            self.course_options = list(self.course_dict.keys())

            # Get timeslots
            self.parent.parent.cursor.execute("""
                SELECT timeslot_id, CONCAT(day, ' ', start_time, '-', end_time) as schedule
                FROM timeslot 
                ORDER BY day, start_time
            """)
            timeslots = self.parent.parent.cursor.fetchall()
            self.timeslot_dict = {f"{schedule} (ID: {id})": id for id, schedule in timeslots}
            self.timeslot_options = list(self.timeslot_dict.keys())

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load form data: {e}")
            self.trainer_dict = {}
            self.trainer_options = []
            self.room_dict = {}
            self.room_options = []
            self.course_dict = {}
            self.course_options = []
            self.timeslot_dict = {}
            self.timeslot_options = []

    def populate_form(self):
        """Populate form with existing class data"""
        if self.class_data:
            # Set gender
            self.entries['gender'].set(self.class_data[0])

            # Find and set trainer
            trainer_id = self.class_data[1]
            for option, tid in self.trainer_dict.items():
                if tid == trainer_id:
                    self.entries['trainer'].set(option)
                    break

            # Find and set room
            room_id = self.class_data[2]
            for option, rid in self.room_dict.items():
                if rid == room_id:
                    self.entries['room'].set(option)
                    break

            # Find and set course
            course_id = self.class_data[3]
            for option, cid in self.course_dict.items():
                if cid == course_id:
                    self.entries['course'].set(option)
                    break

            # Find and set timeslot
            timeslot_id = self.class_data[4]
            for option, tid in self.timeslot_dict.items():
                if tid == timeslot_id:
                    self.entries['timeslot'].set(option)
                    break

            # Set registrants
            self.entries['registrants'].delete(0, tk.END)
            self.entries['registrants'].insert(0, str(self.class_data[5]))

    def save_class(self):
        """Save class data with validation"""
        try:
            # Get and validate form data
            gender = self.entries['gender'].get().strip()
            trainer_selection = self.entries['trainer'].get().strip()
            room_selection = self.entries['room'].get().strip()
            course_selection = self.entries['course'].get().strip()
            timeslot_selection = self.entries['timeslot'].get().strip()
            registrants = self.entries['registrants'].get().strip()

            # Validation
            if not all([gender, trainer_selection, room_selection, course_selection, timeslot_selection, registrants]):
                messagebox.showerror("Validation Error", "All fields are required!")
                return

            # Get IDs from selections
            if trainer_selection not in self.trainer_dict:
                messagebox.showerror("Validation Error", "Please select a valid trainer!")
                return
            trainer_id = self.trainer_dict[trainer_selection]

            if room_selection not in self.room_dict:
                messagebox.showerror("Validation Error", "Please select a valid room!")
                return
            room_id = self.room_dict[room_selection]

            if course_selection not in self.course_dict:
                messagebox.showerror("Validation Error", "Please select a valid course!")
                return
            course_id = self.course_dict[course_selection]

            if timeslot_selection not in self.timeslot_dict:
                messagebox.showerror("Validation Error", "Please select a valid timeslot!")
                return
            timeslot_id = self.timeslot_dict[timeslot_selection]

            # Validate numeric fields
            try:
                registrants = int(registrants)
            except ValueError:
                messagebox.showerror("Validation Error", "Number of registrants must be a number!")
                return

            # Database operations
            if self.class_data:  # Edit existing class
                old_timeslot_id = self.class_data[4]
                old_room_id = self.class_data[2]

                self.parent.parent.cursor.execute("""
                    UPDATE class 
                    SET gender = %s, person_id = %s, room_id = %s, course_id = %s, 
                        timeslot_id = %s, registrants = %s 
                    WHERE timeslot_id = %s AND room_id = %s
                """, (gender, trainer_id, room_id, course_id, timeslot_id, registrants,
                      old_timeslot_id, old_room_id))

                success_msg = "Class updated successfully!"
            else:  # Add new class
                # Check if class already exists (timeslot + room combination)
                self.parent.parent.cursor.execute("""
                    SELECT COUNT(*) FROM class WHERE timeslot_id = %s AND room_id = %s
                """, (timeslot_id, room_id))

                if self.parent.parent.cursor.fetchone()[0] > 0:
                    messagebox.showerror("Validation Error",
                                         "A class already exists for this timeslot and room combination!")
                    return

                self.parent.parent.cursor.execute("""
                    INSERT INTO class (gender, person_id, room_id, course_id, timeslot_id, registrants) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (gender, trainer_id, room_id, course_id, timeslot_id, registrants))

                success_msg = "Class added successfully!"

            self.parent.parent.connection.commit()
            messagebox.showinfo("Success", success_msg)
            self.parent.refresh_classes()
            self.window.destroy()

        except Exception as e:
            self.parent.parent.connection.rollback()
            messagebox.showerror("Database Error", f"Failed to save class: {e}")

class TrainerManagementWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent.root)
        self.window.title("Trainer Management")
        self.window.geometry("1200x800")
        self.window.configure(bg=parent.colors['background'])

        self.window.transient(parent.root)
        self.window.grab_set()

        self.create_modern_interface()
        self.refresh_trainers()

    def create_modern_interface(self):
        """Create modern trainer management interface"""
        # Header
        header_frame = tk.Frame(self.window, bg=self.parent.colors['danger'], height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        header_content = tk.Frame(header_frame, bg=self.parent.colors['danger'])
        header_content.pack(expand=True, fill='both', padx=30)

        icon_label = tk.Label(header_content, text="🏃", font=('Segoe UI Emoji', 24),
                              bg=self.parent.colors['danger'], fg='white')
        icon_label.pack(side=tk.LEFT, pady=25)

        title_label = tk.Label(header_content, text="Trainer Management",
                               font=('Segoe UI', 24, 'bold'),
                               bg=self.parent.colors['danger'], fg='white')
        title_label.pack(side=tk.LEFT, padx=(15, 0), pady=25)

        # Action buttons frame
        buttons_frame = tk.Frame(self.window, bg=self.parent.colors['background'], height=80)
        buttons_frame.pack(fill=tk.X, padx=30, pady=(20, 0))
        buttons_frame.pack_propagate(False)

        # Modern action buttons
        btn_data = [
            ("+ Add Trainer", self.add_trainer, self.parent.colors['success'], "#229954"),
            ("✏️ Edit Trainer", self.edit_trainer, self.parent.colors['accent'], "#2980B9"),
            ("🗑️ Delete Trainer", self.delete_trainer, self.parent.colors['danger'], "#CB4335"),
            ("🔄 Refresh", self.refresh_trainers, self.parent.colors['secondary'], "#34495E")
        ]

        for text, command, color, hover_color in btn_data:
            btn = ModernButton(buttons_frame, text, command, color, hover_color,
                               width=15, height=2)
            btn.pack(side=tk.LEFT, padx=(0, 15), pady=20)

        # Data table frame with card styling
        table_frame = tk.Frame(self.window, bg=self.parent.colors['card'], relief='flat', bd=1)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(10, 30))

        # Treeview with modern styling - תיקון העמודות
        self.tree = ttk.Treeview(table_frame,
                                 columns=('ID', 'Name', 'Gender', 'Birth Date', 'Experience Level'),
                                 show='headings', height=15,
                                 style="Modern.Treeview")

        # Configure columns - תיקון הגדרת העמודות
        columns_config = [
            ('ID', 70, 'ID'),
            ('Name', 200, 'Trainer Name'),
            ('Gender', 80, 'Gender'),
            ('Birth Date', 120, 'Birth Date'),
            ('Experience Level', 150, 'Experience Level')
        ]

        for col_id, width, heading in columns_config:
            self.tree.heading(col_id, text=heading)
            self.tree.column(col_id, width=width, anchor='center')

        # Scrollbars
        v_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)

        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack everything
        self.tree.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        v_scrollbar.grid(row=0, column=1, sticky='ns', pady=20)
        h_scrollbar.grid(row=1, column=0, sticky='ew', padx=20)

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

    def refresh_trainers(self):
        """Refresh the trainers list - תיקון השאילתה"""
        try:
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Query trainers - שאילתה מתוקנת
            query = """
            SELECT t.person_id, p.person_name, p.gender, p.birth_date, 
                   t.experiencelevel
            FROM Trainer t
            JOIN Person p ON t.person_id = p.person_id
            ORDER BY t.person_id
            """
            self.parent.cursor.execute(query)
            trainers = self.parent.cursor.fetchall()

            # Insert into treeview with alternating colors
            for i, trainer in enumerate(trainers):
                # Format the data properly
                formatted_trainer = list(trainer)
                # Format birth date
                if formatted_trainer[3]:
                    formatted_trainer[3] = str(formatted_trainer[3])
                else:
                    formatted_trainer[3] = 'N/A'

                # Convert experience level to readable format
                experience_levels = {1: 'Beginner', 2: 'Intermediate', 3: 'Advanced'}
                if formatted_trainer[4] in experience_levels:
                    formatted_trainer[4] = experience_levels[formatted_trainer[4]]
                else:
                    formatted_trainer[4] = str(formatted_trainer[4])

                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                self.tree.insert('', 'end', values=formatted_trainer, tags=(tag,))

            # Configure row colors
            self.tree.tag_configure('evenrow', background='#F8F9FA')
            self.tree.tag_configure('oddrow', background='#FFFFFF')

        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh trainers: {e}")

    def add_trainer(self):
        """Add new trainer"""
        TrainerFormWindow(self, "Add New Trainer")

    def edit_trainer(self):
        """Edit selected trainer"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a trainer to edit")
            return

        item = self.tree.item(selection[0])
        trainer_data = item['values']
        TrainerFormWindow(self, "Edit Trainer", trainer_data)

    def delete_trainer(self):
        """Delete selected trainer with confirmation"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a trainer to delete")
            return

        item = self.tree.item(selection[0])
        trainer_id = item['values'][0]
        trainer_name = item['values'][1]

        if messagebox.askyesno("Confirm Deletion",
                               f"Are you sure you want to delete trainer:\n{trainer_name} (ID: {trainer_id})?",
                               icon='warning'):
            try:
                # Delete with proper foreign key handling
                self.parent.cursor.execute("DELETE FROM certified_for WHERE person_id = %s", (trainer_id,))
                self.parent.cursor.execute("UPDATE class SET person_id = NULL WHERE person_id = %s", (trainer_id,))
                self.parent.cursor.execute("DELETE FROM Trainer WHERE person_id = %s", (trainer_id,))
                self.parent.cursor.execute("DELETE FROM Person WHERE person_id = %s", (trainer_id,))

                self.parent.connection.commit()
                messagebox.showinfo("Success", f"Trainer {trainer_name} deleted successfully!")
                self.refresh_trainers()

            except Exception as e:
                self.parent.connection.rollback()
                messagebox.showerror("Error", f"Failed to delete trainer: {e}")


class TrainerFormWindow:
    def __init__(self, parent, title, trainer_data=None):

        self.parent = parent
        self.trainer_data = trainer_data
        self.window = tk.Toplevel(parent.window)
        self.window.title(title)
        self.window.geometry("500x600")
        self.window.configure(bg=parent.parent.colors['background'])

        # Make window modal
        self.window.transient(parent.window)
        self.window.grab_set()

        # Center the window
        self.window.geometry("+%d+%d" % (parent.window.winfo_rootx() + 350,
                                         parent.window.winfo_rooty() + 100))

        self.create_modern_form()

        if trainer_data:
            self.populate_form()

    def create_modern_form(self):
        """Create modern trainer form"""
        # Header
        header_frame = tk.Frame(self.window, bg=self.parent.parent.colors['danger'], height=70)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        title_label = tk.Label(header_frame, text="Trainer Information",
                               font=('Segoe UI', 20, 'bold'),
                               bg=self.parent.parent.colors['danger'], fg='white')
        title_label.pack(expand=True)

        # Form container
        form_container = tk.Frame(self.window, bg=self.parent.parent.colors['card'])
        form_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        # Form fields
        fields_config = [
            ("Full Name", "name", "entry"),
            ("Gender", "gender", "combo", None, ['M', 'F']),
            ("Birth Date", "birth_date", "entry", "Format: YYYY-MM-DD"),
            ("Experience Level", "experiencelevel", "combo", None, ['Beginner', 'Intermediate', 'Advanced'])
        ]

        self.entries = {}

        for i, field_config in enumerate(fields_config):
            field_name = field_config[0]
            field_key = field_config[1]
            field_type = field_config[2]
            field_hint = field_config[3] if len(field_config) > 3 else None
            field_values = field_config[4] if len(field_config) > 4 else None

            # Field container
            field_frame = tk.Frame(form_container, bg=self.parent.parent.colors['card'])
            field_frame.pack(fill=tk.X, pady=(0, 20))

            # Label
            label = tk.Label(field_frame, text=field_name,
                             font=('Segoe UI', 12, 'bold'),
                             bg=self.parent.parent.colors['card'],
                             fg=self.parent.parent.colors['primary'])
            label.pack(anchor=tk.W)

            # Hint
            if field_hint:
                hint_label = tk.Label(field_frame, text=field_hint,
                                      font=('Segoe UI', 9),
                                      bg=self.parent.parent.colors['card'],
                                      fg=self.parent.parent.colors['secondary'])
                hint_label.pack(anchor=tk.W)

            # Input field
            if field_type == "combo":
                self.entries[field_key] = ttk.Combobox(
                    field_frame, values=field_values,
                    font=('Segoe UI', 11), height=12
                )
            else:
                self.entries[field_key] = tk.Entry(
                    field_frame, font=('Segoe UI', 11),
                    relief='flat', bd=5,
                    bg=self.parent.parent.colors['light'],
                    fg=self.parent.parent.colors['primary']
                )

            self.entries[field_key].pack(fill=tk.X, pady=(6, 0))

        # Buttons frame
        buttons_frame = tk.Frame(form_container, bg=self.parent.parent.colors['card'], height=80)
        buttons_frame.pack(fill=tk.X, pady=(30, 0))

        # Action buttons
        save_btn = ModernButton(buttons_frame, "💾 Save Trainer", self.save_trainer,
                                self.parent.parent.colors['success'], "#229954",
                                width=15, height=2)
        save_btn.pack(side=tk.RIGHT, padx=(10, 0))

        cancel_btn = ModernButton(buttons_frame, "❌ Cancel", self.window.destroy,
                                  self.parent.parent.colors['secondary'], "#34495E",
                                  width=15, height=2)
        cancel_btn.pack(side=tk.RIGHT, pady=10)

    def populate_form(self):
        """Populate form with existing trainer data - תיקון הפונקציה"""
        if self.trainer_data:
            print("Trainer data:", self.trainer_data)
            self.entries['name'].insert(0, self.trainer_data[1])
            self.entries['gender'].set(self.trainer_data[2])
            self.entries['birth_date'].insert(0, str(self.trainer_data[3]))

            # Convert experience level back to text
            experience_level = self.trainer_data[4]
            if experience_level in ['Beginner', 'Intermediate', 'Advanced']:
                self.entries['experiencelevel'].set(experience_level)
            else:
                # If it's a number, convert it
                experience_levels = {1: 'Beginner', 2: 'Intermediate', 3: 'Advanced'}
                if experience_level in experience_levels:
                    self.entries['experiencelevel'].set(experience_levels[experience_level])
                else:
                    self.entries['experiencelevel'].set('Beginner')

    def save_trainer(self):
        """Save trainer data with validation - תיקון הפונקציה"""
        try:
            # Get and validate form data
            name = self.entries['name'].get().strip()
            gender = self.entries['gender'].get().strip()
            birth_date = self.entries['birth_date'].get().strip()
            experience_level_text = self.entries['experiencelevel'].get().strip()

            # Validation
            if not all([name, gender, birth_date, experience_level_text]):
                messagebox.showerror("Validation Error", "All fields are required!")
                return

            # Convert experience level to number
            experience_levels = {'Beginner': 1, 'Intermediate': 2, 'Advanced': 3}
            experience_level = experience_levels.get(experience_level_text, 1)

            # Database operations
            if self.trainer_data:  # Edit existing trainer
                trainer_id = self.trainer_data[0]

                # Update Person table
                self.parent.parent.cursor.execute(
                    "UPDATE Person SET person_name = %s, gender = %s, birth_date = %s WHERE person_id = %s",
                    (name, gender, birth_date, trainer_id)
                )

                # Update Trainer table
                self.parent.parent.cursor.execute(
                    "UPDATE Trainer SET experiencelevel = %s WHERE person_id = %s",
                    (experience_level, trainer_id)
                )

                success_msg = f"Trainer {name} updated successfully!"
            else:  # Add new trainer
                # שלב 1: קבלת ה-id הכי גבוה
                self.parent.parent.cursor.execute("SELECT COALESCE(MAX(person_id), 0) FROM Person")
                person_id = self.parent.parent.cursor.fetchone()[0] + 1

                # שלב 2: הכנסת האדם עם המזהה
                self.parent.parent.cursor.execute(
                    "INSERT INTO Person (person_id, person_name, gender, birth_date) VALUES (%s, %s, %s, %s)",
                    (person_id, name, gender, birth_date)
                )

                # שלב 3: הכנסת המאמן
                self.parent.parent.cursor.execute(
                    "INSERT INTO Trainer (person_id, experiencelevel) VALUES (%s, %s)",
                    (person_id, experience_level)
                )

                success_msg = f"Trainer {name} added successfully!"

            self.parent.parent.connection.commit()
            messagebox.showinfo("Success", success_msg)
            self.parent.refresh_trainers()
            self.window.destroy()

        except Exception as e:
            self.parent.parent.connection.rollback()
            messagebox.showerror("Database Error", f"Failed to save trainer: {e}")
class AnalyticsWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent.root)
        self.window.title("Analytics & Reports")
        self.window.geometry("900x700")
        self.window.configure(bg='#f0f0f0')

        self.create_interface()

    def create_interface(self):
        """Create analytics interface"""
        # Title
        title_label = tk.Label(self.window, text="Analytics & Reports",
                              font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=10)

        # Buttons frame
        buttons_frame = tk.Frame(self.window, bg='#f0f0f0')
        buttons_frame.pack(pady=20)

        # Query buttons
        tk.Button(buttons_frame, text="Member Statistics", command=self.show_member_stats,
                 bg='#3498db', fg='white', font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=10)
        tk.Button(buttons_frame, text="Active Classes Report", command=self.show_active_classes,
                 bg='#2ecc71', fg='white', font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=10)
        tk.Button(buttons_frame, text="Trainer Schedule", command=self.show_trainer_schedule,
                 bg='#e74c3c', fg='white', font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=10)

        # Results frame with scrollbar
        results_frame = tk.Frame(self.window, bg='#f0f0f0')
        results_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Text widget for results
        self.results_text = tk.Text(results_frame, wrap=tk.WORD, font=('Arial', 10))
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)

        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def show_member_stats(self):
        """Show member statistics using the analyze_member_statistics function"""
        try:
            # Call the function
            self.parent.cursor.execute("SELECT analyze_member_statistics()")
            cursor_name = self.parent.cursor.fetchone()[0]

            # Fetch results from cursor
            self.parent.cursor.execute(f"FETCH ALL FROM \"{cursor_name}\"")
            results = self.parent.cursor.fetchall()

            # Display results
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "=== MEMBER STATISTICS ===\n\n")

            for row in results:
                analysis_type, metric_name, metric_value, details = row
                self.results_text.insert(tk.END, f"{analysis_type} - {metric_name}: {metric_value}\n")
                self.results_text.insert(tk.END, f"Details: {details}\n\n")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to get member statistics: {e}")

    def show_active_classes(self):
        """Show active classes report"""
        try:
            query = """
            SELECT c.course_name, ts.day, ts.start_time, ts.end_time, 
                   r.room_name, cl.registrants, p.person_name as trainer_name
            FROM Class cl
            JOIN Course c ON cl.course_id = c.course_id
            JOIN TimeSlot ts ON cl.timeslot_id = ts.timeslot_id
            JOIN Room r ON cl.room_id = r.room_id
            JOIN Person p ON cl.person_id = p.person_id
            WHERE cl.registrants > 0
            ORDER BY ts.day, ts.start_time
            """

            self.parent.cursor.execute(query)
            results = self.parent.cursor.fetchall()

            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "=== ACTIVE CLASSES REPORT ===\n\n")

            for row in results:
                course_name, day, start_time, end_time, room_name, registrants, trainer_name = row
                self.results_text.insert(tk.END, f"Course: {course_name}\n")
                self.results_text.insert(tk.END, f"Schedule: {day} {start_time} - {end_time}\n")
                self.results_text.insert(tk.END, f"Room: {room_name}\n")
                self.results_text.insert(tk.END, f"Trainer: {trainer_name}\n")
                self.results_text.insert(tk.END, f"Registrants: {registrants}\n")
                self.results_text.insert(tk.END, "-" * 40 + "\n\n")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to get active classes: {e}")

    def show_trainer_schedule(self):
        """Show trainer schedule - with trainer selection dialog"""
        # Get trainer list first
        try:
            self.parent.cursor.execute("""
                SELECT t.person_id, p.person_name 
                FROM Trainer t 
                JOIN Person p ON t.person_id = p.person_id 
                ORDER BY p.person_name
            """)
            trainers = self.parent.cursor.fetchall()
            # try:
            #     self.parent.cursor.execute("CLOSE schedule_cursor")
            # except Exception as e:
            #     trainers = trainers
            if not trainers:
                messagebox.showinfo("Info", "No trainers found")
                return

            # Create selection dialog
            TrainerSelectionDialog(self, trainers)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to get trainers: {e}")

class TrainerSelectionDialog:
    def __init__(self, parent, trainers):
        self.parent = parent
        self.trainers = trainers
        self.window = tk.Toplevel(parent.window)
        self.window.title("Select Trainer")
        self.window.geometry("300x400")
        self.window.configure(bg='#f0f0f0')

        self.create_interface()

    def create_interface(self):
        """Create trainer selection interface"""
        # Title
        title_label = tk.Label(self.window, text="Select Trainer for Schedule",
                              font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=10)

        # Listbox for trainers
        self.trainer_listbox = tk.Listbox(self.window, font=('Arial', 11))
        self.trainer_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Populate listbox
        for trainer_id, trainer_name in self.trainers:
            self.trainer_listbox.insert(tk.END, f"{trainer_name} (ID: {trainer_id})")

        # Buttons
        buttons_frame = tk.Frame(self.window, bg='#f0f0f0')
        buttons_frame.pack(pady=10)

        tk.Button(buttons_frame, text="Show Schedule", command=self.show_schedule,
                 bg='#3498db', fg='white', font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=10)
        tk.Button(buttons_frame, text="Cancel", command=self.window.destroy,
                 bg='#95a5a6', fg='white', font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=10)

    def show_schedule(self):
        """Show selected trainer's schedule"""
        selection = self.trainer_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a trainer")
            return

        selected_trainer = self.trainers[selection[0]]
        trainer_id = selected_trainer[0]
        trainer_name = selected_trainer[1]

        try:
            # Call the get_trainer_schedule function
            self.parent.parent.cursor.execute("SELECT get_trainer_schedule(%s)", (trainer_id,))
            cursor_name = self.parent.parent.cursor.fetchone()[0]

            # Fetch results from cursor
            self.parent.parent.cursor.execute(f"FETCH ALL FROM \"{cursor_name}\"")
            results = self.parent.parent.cursor.fetchall()

            # Display results in parent window
            self.parent.results_text.delete(1.0, tk.END)
            self.parent.results_text.insert(tk.END, f"=== TRAINER SCHEDULE: {trainer_name} ===\n\n")

            if not results:
                self.parent.results_text.insert(tk.END, "No classes scheduled for this trainer.\n")
            else:
                for row in results:
                    course_name, day, start_time, end_time, room_name, registrants, status = row
                    self.parent.results_text.insert(tk.END, f"Course: {course_name}\n")
                    self.parent.results_text.insert(tk.END, f"Day: {day}\n")
                    self.parent.results_text.insert(tk.END, f"Time: {start_time} - {end_time}\n")
                    self.parent.results_text.insert(tk.END, f"Room: {room_name}\n")
                    self.parent.results_text.insert(tk.END, f"Registrants: {registrants}\n")
                    self.parent.results_text.insert(tk.END, f"Status: {status}\n")
                    self.parent.results_text.insert(tk.END, "-" * 40 + "\n\n")

            self.window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to get trainer schedule: {e}")


class FunctionsWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent.root)
        self.window.title("Database Functions")
        self.window.geometry("800x600")
        self.window.configure(bg='#f0f0f0')

        self.create_interface()

    def create_interface(self):
        """Create database functions interface"""
        # Title
        title_label = tk.Label(self.window, text="Database Functions & Procedures",
                               font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=10)

        # Functions frame
        functions_frame = tk.Frame(self.window, bg='#f0f0f0')
        functions_frame.pack(pady=20)

        # Query buttons
        tk.Button(functions_frame, text="Trainer Classes Report", command=self.trainer_classes_report,
                  bg='#3498db', fg='white', font=('Arial', 12, 'bold')).pack(pady=10)
        tk.Button(functions_frame, text="Members Expiring Next Month", command=self.members_expiring_next_month,
                  bg='#9b59b6', fg='white', font=('Arial', 12, 'bold')).pack(pady=10)
        tk.Button(functions_frame, text="Fix Broken Equipment", command=self.fix_broken_equipment,
                  bg='#e74c3c', fg='white', font=('Arial', 12, 'bold')).pack(pady=10)

        # Results text area
        results_frame = tk.Frame(self.window, bg='#f0f0f0')
        results_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.results_text = tk.Text(results_frame, wrap=tk.WORD, font=('Arial', 10))
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)

        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def trainer_classes_report(self):
        """Execute trainer classes report query"""
        try:
            query = """
            SELECT 
              T.person_id AS TrainerId,
              P.person_name AS TrainerName,
              COUNT(*) AS WeeklyClasses
            FROM 
              Trainer T
            JOIN 
              Person P ON T.person_id = P.person_id
            JOIN 
              Class C ON C.person_id = T.person_id
            GROUP BY 
              T.person_id, P.person_name
            ORDER BY 
              WeeklyClasses DESC;
            """

            self.parent.cursor.execute(query)
            results = self.parent.cursor.fetchall()

            # Display results
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "=== TRAINER CLASSES REPORT ===\n\n")
            self.results_text.insert(tk.END, f"{'Trainer ID':<12} {'Trainer Name':<20} {'Weekly Classes':<15}\n")
            self.results_text.insert(tk.END, "-" * 50 + "\n")

            if results:
                for row in results:
                    trainer_id, trainer_name, weekly_classes = row
                    self.results_text.insert(tk.END, f"{trainer_id:<12} {trainer_name:<20} {weekly_classes:<15}\n")
            else:
                self.results_text.insert(tk.END, "No trainers found with assigned classes.\n")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to execute trainer classes report: {e}")

    def members_expiring_next_month(self):
        """Execute members expiring next month query"""
        try:
            query = """
            SELECT 
              M.person_id AS MemberId,
              P.person_name AS MemberName,
              M.ExpirationDate
            FROM 
              Member M
            JOIN 
              Person P ON M.person_id = P.person_id
            WHERE 
              EXTRACT(MONTH FROM M.ExpirationDate) = EXTRACT(MONTH FROM CURRENT_DATE + INTERVAL '1 month')
              AND EXTRACT(YEAR FROM M.ExpirationDate) = EXTRACT(YEAR FROM CURRENT_DATE + INTERVAL '1 month')
            ORDER BY 
              M.ExpirationDate;
            """

            self.parent.cursor.execute(query)
            results = self.parent.cursor.fetchall()

            # Display results
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "=== MEMBERS EXPIRING NEXT MONTH ===\n\n")
            self.results_text.insert(tk.END, f"{'Member ID':<12} {'Member Name':<20} {'Expiration Date':<15}\n")
            self.results_text.insert(tk.END, "-" * 50 + "\n")

            if results:
                for row in results:
                    member_id, member_name, expiration_date = row
                    self.results_text.insert(tk.END, f"{member_id:<20} {member_name:<50} {expiration_date}\n")
            else:
                self.results_text.insert(tk.END, "No members found with subscriptions expiring next month.\n")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to execute members expiring query: {e}")

    def fix_broken_equipment(self):
        """Fix broken equipment procedure"""
        try:
            # Call the procedure
            self.parent.cursor.execute("CALL fix_broken_equipment()")
            self.parent.connection.commit()

            # Display success message
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "=== EQUIPMENT REPAIR COMPLETED ===\n\n")
            self.results_text.insert(tk.END, "All broken equipment has been repaired successfully!\n")
            self.results_text.insert(tk.END, "Equipment status updated to working condition.\n")

            messagebox.showinfo("Success", "Equipment repair procedure completed successfully!")

        except Exception as e:
            self.parent.connection.rollback()
            messagebox.showerror("Error", f"Failed to fix equipment: {e}")

class MemberRegistrationDialog:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent.window)
        self.window.title("Register Member to Class")
        self.window.geometry("400x300")
        self.window.configure(bg='#f0f0f0')

        self.create_interface()
        self.load_data()

    def create_interface(self):
        """Create member registration interface"""
        # Title
        title_label = tk.Label(self.window, text="Register Member to Class",
                              font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=10)

        # Form frame
        form_frame = tk.Frame(self.window, bg='#f0f0f0')
        form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Member selection
        tk.Label(form_frame, text="Select Member:", font=('Arial', 12),
                bg='#f0f0f0', fg='#2c3e50').pack(anchor=tk.W, pady=(10, 0))
        self.member_combo = ttk.Combobox(form_frame, font=('Arial', 11), state="readonly")
        self.member_combo.pack(fill=tk.X, pady=(0, 10))

        # Course selection
        tk.Label(form_frame, text="Select Course:", font=('Arial', 12),
                bg='#f0f0f0', fg='#2c3e50').pack(anchor=tk.W, pady=(10, 0))
        self.course_combo = ttk.Combobox(form_frame, font=('Arial', 11), state="readonly")
        self.course_combo.pack(fill=tk.X, pady=(0, 10))

        # Buttons
        buttons_frame = tk.Frame(form_frame, bg='#f0f0f0')
        buttons_frame.pack(pady=20)

        tk.Button(buttons_frame, text="Register", command=self.register_member,
                 bg='#2ecc71', fg='white', font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=10)
        tk.Button(buttons_frame, text="Cancel", command=self.window.destroy,
                 bg='#95a5a6', fg='white', font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=10)

    def load_data(self):
        """Load members and courses data"""
        try:
            # Load members
            self.parent.parent.cursor.execute("""
                SELECT m.person_id, p.person_name 
                FROM Member m 
                JOIN Person p ON m.person_id = p.person_id 
                WHERE m.expirationdate > CURRENT_DATE
                ORDER BY p.person_name
            """)
            members = self.parent.parent.cursor.fetchall()

            member_list = [f"{name} (ID: {id})" for id, name in members]
            self.member_combo['values'] = member_list
            self.members_data = members

            # Load courses
            self.parent.parent.cursor.execute("""
                SELECT course_id, course_name 
                FROM Course 
                ORDER BY course_name
            """)
            courses = self.parent.parent.cursor.fetchall()

            course_list = [f"{name} (ID: {id})" for id, name in courses]
            self.course_combo['values'] = course_list
            self.courses_data = courses

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

    def register_member(self):
        """Register selected member to selected course"""
        if not self.member_combo.get() or not self.course_combo.get():
            messagebox.showerror("Error", "Please select both member and course")
            return

        try:
            # Get selected member and course IDs
            member_index = self.member_combo.current()
            course_index = self.course_combo.current()

            member_id = self.members_data[member_index][0]
            course_id = self.courses_data[course_index][0]

            # Call the registration procedure
            self.parent.parent.cursor.execute(
                "CALL register_member_to_class(%s, %s)",
                (course_id, member_id)
            )
            self.parent.parent.connection.commit()

            # Display success message
            member_name = self.members_data[member_index][1]
            course_name = self.courses_data[course_index][1]

            self.parent.results_text.delete(1.0, tk.END)
            self.parent.results_text.insert(tk.END, "=== MEMBER REGISTRATION SUCCESSFUL ===\n\n")
            self.parent.results_text.insert(tk.END, f"Member: {member_name} (ID: {member_id})\n")
            self.parent.results_text.insert(tk.END, f"Course: {course_name} (ID: {course_id})\n")
            self.parent.results_text.insert(tk.END, f"Registration completed successfully!\n")

            messagebox.showinfo("Success", f"Member {member_name} registered to {course_name} successfully!")
            self.window.destroy()

        except Exception as e:
            self.parent.parent.connection.rollback()
            messagebox.showerror("Error", f"Registration failed: {e}")


# ===================================== RegistrationManagementWindow ==================================

# Modern design pattern for registration management windows...
class RegistrationManagementWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent.root)
        self.window.title("Registration Management")
        self.window.geometry("1200x700")
        self.window.configure(bg=parent.colors['background'])

        self.window.transient(parent.root)
        self.window.grab_set()

        self.create_modern_interface()
        self.refresh_registrations()

    def create_modern_interface(self):
        """Create modern registration management interface"""
        # Header
        header_frame = tk.Frame(self.window, bg=self.parent.colors['success'], height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        header_content = tk.Frame(header_frame, bg=self.parent.colors['success'])
        header_content.pack(expand=True, fill='both', padx=30)

        icon_label = tk.Label(header_content, text="📝", font=('Segoe UI Emoji', 24),
                              bg=self.parent.colors['success'], fg='white')
        icon_label.pack(side=tk.LEFT, pady=25)

        title_label = tk.Label(header_content, text="Registration Management",
                               font=('Segoe UI', 24, 'bold'),
                               bg=self.parent.colors['success'], fg='white')
        title_label.pack(side=tk.LEFT, padx=(15, 0), pady=25)

        # Search and filter frame
        filter_frame = tk.Frame(self.window, bg=self.parent.colors['background'], height=60)
        filter_frame.pack(fill=tk.X, padx=30, pady=(10, 0))
        filter_frame.pack_propagate(False)

        # Search entry
        tk.Label(filter_frame, text="Search:", font=('Segoe UI', 10, 'bold'),
                 bg=self.parent.colors['background'], fg=self.parent.colors['primary']).pack(side=tk.LEFT, pady=20)

        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(filter_frame, textvariable=self.search_var, font=('Segoe UI', 10),
                                     width=30, relief='flat', bd=5)
        self.search_entry.pack(side=tk.LEFT, padx=(10, 20), pady=20)
        self.search_entry.bind('<KeyRelease>', self.on_search)

        # Action buttons frame
        buttons_frame = tk.Frame(self.window, bg=self.parent.colors['background'], height=80)
        buttons_frame.pack(fill=tk.X, padx=30, pady=(10, 0))
        buttons_frame.pack_propagate(False)

        # Modern action buttons
        btn_data = [
            ("+ Add Registration", self.add_registration, self.parent.colors['success'], "#229954"),
            ("✏️ Edit Registration", self.edit_registration, self.parent.colors['accent'], "#2980B9"),
            ("🗑️ Remove Registration", self.delete_registration, self.parent.colors['danger'], "#CB4335"),
            ("🔄 Refresh", self.refresh_registrations, self.parent.colors['secondary'], "#34495E")
        ]

        for text, command, color, hover_color in btn_data:
            btn = ModernButton(buttons_frame, text, command, color, hover_color,
                               width=18, height=2)
            btn.pack(side=tk.LEFT, padx=(0, 15), pady=20)

        # Data table frame with card styling
        table_frame = tk.Frame(self.window, bg=self.parent.colors['card'], relief='flat', bd=1)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(10, 30))

        # Treeview with modern styling
        self.tree = ttk.Treeview(table_frame,
                                 columns=('Person', 'Email', 'Phone', 'Class', 'Room', 'Timeslot', 'Course'),
                                 show='headings', height=15,
                                 style="Modern.Treeview")

        # Configure columns
        columns_config = [
            ('Person', 200, 'Person Name'),
            ('Email', 200, 'Email'),
            ('Phone', 120, 'Phone'),
            ('Class', 100, 'Class Type'),
            ('Room', 120, 'Room'),
            ('Timeslot', 200, 'Time Schedule'),
            ('Course', 180, 'Course Name')
        ]

        for col_id, width, heading in columns_config:
            self.tree.heading(col_id, text=heading)
            self.tree.column(col_id, width=width, anchor='center')

        # Scrollbars
        v_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)

        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack everything
        self.tree.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        v_scrollbar.grid(row=0, column=1, sticky='ns', pady=20)
        h_scrollbar.grid(row=1, column=0, sticky='ew', padx=20)

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

    def refresh_registrations(self):
        """Refresh the registrations list"""
        try:
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Query registrations with all related information
            query = """
            SELECT 
                p.person_name,
                p.email,
                p.phone,
                cl.gender AS class_type,
                r.room_name,
                CONCAT(ts.day, ' ', ts.start_time, '-', ts.end_time) AS timeslot,
                co.course_name,
                rf.person_id,
                rf.timeslot_id,
                rf.room_id
            FROM registers_for rf
            JOIN person p ON rf.person_id = p.person_id
            JOIN timeslot ts ON rf.timeslot_id = ts.timeslot_id
            JOIN room r ON rf.room_id = r.room_id
            LEFT JOIN class cl ON (cl.timeslot_id = rf.timeslot_id AND cl.room_id = rf.room_id)
            LEFT JOIN course co ON cl.course_id = co.course_id
            ORDER BY p.person_name, ts.day, ts.start_time;
            """
            self.parent.cursor.execute(query)
            registrations = self.parent.cursor.fetchall()

            # Store full data for operations
            self.registration_data = {}

            # Insert into treeview with alternating colors
            for i, reg_data in enumerate(registrations):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                # Display first 7 columns
                display_values = reg_data[:7]
                item_id = self.tree.insert('', 'end', values=display_values, tags=(tag,))

                # Store full data including IDs
                self.registration_data[item_id] = {
                    'person_id': reg_data[7],
                    'timeslot_id': reg_data[8],
                    'room_id': reg_data[9],
                    'person_name': reg_data[0],
                    'room_name': reg_data[4],
                    'timeslot': reg_data[5]
                }

            # Configure row colors
            self.tree.tag_configure('evenrow', background='#F8F9FA')
            self.tree.tag_configure('oddrow', background='#FFFFFF')

            # Update status
            total_registrations = len(registrations)
            if hasattr(self, 'status_label'):
                self.status_label.config(text=f"Total Registrations: {total_registrations}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh registrations: {e}")

    def on_search(self, event=None):
        """Filter registrations based on search term"""
        search_term = self.search_var.get().lower()

        # Clear and repopulate tree with filtered results
        for item in self.tree.get_children():
            values = self.tree.item(item)['values']
            # Check if search term appears in any visible column
            if any(search_term in str(value).lower() for value in values):
                self.tree.reattach(item, '', 'end')
            else:
                self.tree.detach(item)

    def add_registration(self):
        """Add new registration"""
        RegistrationFormWindow(self, "Add New Registration")

    def edit_registration(self):
        """Edit selected registration"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a registration to edit")
            return

        item_id = selection[0]
        if item_id in self.registration_data:
            reg_data = self.registration_data[item_id]
            RegistrationFormWindow(self, "Edit Registration", reg_data)
        else:
            messagebox.showerror("Error", "Could not find registration data for editing")

    def delete_registration(self):
        """Delete selected registration with confirmation"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a registration to remove")
            return

        item_id = selection[0]
        if item_id not in self.registration_data:
            messagebox.showerror("Error", "Could not find registration data")
            return

        reg_data = self.registration_data[item_id]
        person_name = reg_data['person_name']
        room_name = reg_data['room_name']
        timeslot = reg_data['timeslot']

        if messagebox.askyesno("Confirm Removal",
                               f"Are you sure you want to remove registration:\n"
                               f"Person: {person_name}\n"
                               f"Room: {room_name}\n"
                               f"Time: {timeslot}?",
                               icon='warning'):
            try:
                self.parent.cursor.execute("""
                    DELETE FROM registers_for 
                    WHERE person_id = %s AND timeslot_id = %s AND room_id = %s
                """, (reg_data['person_id'], reg_data['timeslot_id'], reg_data['room_id']))

                self.parent.connection.commit()
                messagebox.showinfo("Success", "Registration removed successfully!")
                self.refresh_registrations()

            except Exception as e:
                self.parent.connection.rollback()
                messagebox.showerror("Error", f"Failed to remove registration: {e}")


class RegistrationFormWindow:
    def __init__(self, parent, title, registration_data=None):
        self.parent = parent
        self.registration_data = registration_data
        self.window = tk.Toplevel(parent.window)
        self.window.title(title)
        self.window.geometry("500x600")
        self.window.configure(bg=parent.parent.colors['background'])

        # Make window modal
        self.window.transient(parent.window)
        self.window.grab_set()

        # Center the window
        self.window.geometry("+%d+%d" % (parent.window.winfo_rootx() + 350,
                                         parent.window.winfo_rooty() + 100))

        self.create_modern_form()

        if registration_data:
            self.populate_form()

    def create_modern_form(self):
        """Create modern registration form"""
        # Header
        header_frame = tk.Frame(self.window, bg=self.parent.parent.colors['success'], height=70)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        title_label = tk.Label(header_frame, text="Registration Information",
                               font=('Segoe UI', 20, 'bold'),
                               bg=self.parent.parent.colors['success'], fg='white')
        title_label.pack(expand=True)

        # Form container
        form_container = tk.Frame(self.window, bg=self.parent.parent.colors['card'])
        form_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        # Get data for dropdowns
        self.get_form_data()

        # Form fields
        self.entries = {}

        # Person Selection
        self.create_form_field(form_container, "Person", "person", "combo",
                               values=self.person_options, hint="Select person to register")

        # Available Classes (Timeslot + Room combinations)
        self.create_form_field(form_container, "Available Class", "class", "combo",
                               values=self.class_options, hint="Select class to register for")

        # Display class details when selected
        self.class_details_frame = tk.Frame(form_container, bg=self.parent.parent.colors['card'])
        self.class_details_frame.pack(fill=tk.X, pady=(10, 20))

        self.class_details_label = tk.Label(self.class_details_frame,
                                            text="Select a class to see details",
                                            font=('Segoe UI', 10),
                                            bg=self.parent.parent.colors['card'],
                                            fg=self.parent.parent.colors['secondary'])
        self.class_details_label.pack(anchor=tk.W)

        # Bind class selection to show details
        if 'class' in self.entries:
            self.entries['class'].bind('<<ComboboxSelected>>', self.show_class_details)

        # Buttons frame
        buttons_frame = tk.Frame(form_container, bg=self.parent.parent.colors['card'])
        buttons_frame.pack(fill=tk.X, pady=(30, 0))

        # Action buttons
        save_btn = ModernButton(buttons_frame, "💾 Save Registration", self.save_registration,
                                self.parent.parent.colors['success'], "#229954",
                                width=18, height=2)
        save_btn.pack(side=tk.RIGHT, padx=(10, 0))

        cancel_btn = ModernButton(buttons_frame, "❌ Cancel", self.window.destroy,
                                  self.parent.parent.colors['secondary'], "#34495E",
                                  width=15, height=2)
        cancel_btn.pack(side=tk.RIGHT)

    def create_form_field(self, parent, label_text, field_key, field_type, hint=None, values=None):
        """Create a form field with consistent styling"""
        # Field container
        field_frame = tk.Frame(parent, bg=self.parent.parent.colors['card'])
        field_frame.pack(fill=tk.X, pady=(0, 20))

        # Label
        label = tk.Label(field_frame, text=label_text,
                         font=('Segoe UI', 12, 'bold'),
                         bg=self.parent.parent.colors['card'],
                         fg=self.parent.parent.colors['primary'])
        label.pack(anchor=tk.W)

        # Hint
        if hint:
            hint_label = tk.Label(field_frame, text=hint,
                                  font=('Segoe UI', 9),
                                  bg=self.parent.parent.colors['card'],
                                  fg=self.parent.parent.colors['secondary'])
            hint_label.pack(anchor=tk.W)

        # Input field
        if field_type == "combo":
            self.entries[field_key] = ttk.Combobox(
                field_frame, values=values if values else [],
                font=('Segoe UI', 11), height=12, state="readonly"
            )
        else:
            self.entries[field_key] = tk.Entry(
                field_frame, font=('Segoe UI', 11),
                relief='flat', bd=5,
                bg=self.parent.parent.colors['light'],
                fg=self.parent.parent.colors['primary']
            )

        self.entries[field_key].pack(fill=tk.X, pady=(5, 0))

    def get_form_data(self):
        """Get data for form dropdowns"""
        try:
            # Get all persons (could be members or potential members)
            self.parent.parent.cursor.execute("""
                SELECT person_id, person_name, email 
                FROM person 
                ORDER BY person_name
            """)
            persons = self.parent.parent.cursor.fetchall()
            self.person_dict = {f"{name} - {email} (ID: {id})": id for id, name, email in persons}
            self.person_options = list(self.person_dict.keys())

            # Get available classes (from class table - timeslot + room combinations)
            self.parent.parent.cursor.execute("""
                SELECT 
                    cl.timeslot_id,
                    cl.room_id,
                    CONCAT(ts.day, ' ', ts.start_time, '-', ts.end_time) AS schedule,
                    r.room_name,
                    co.course_name,
                    cl.registrants,
                    r.capacity,
                    cl.gender
                FROM class cl
                JOIN timeslot ts ON cl.timeslot_id = ts.timeslot_id
                JOIN room r ON cl.room_id = r.room_id
                LEFT JOIN course co ON cl.course_id = co.course_id
                ORDER BY ts.day, ts.start_time, r.room_name
            """)
            classes = self.parent.parent.cursor.fetchall()

            self.class_dict = {}
            self.class_options = []

            for timeslot_id, room_id, schedule, room_name, course_name, registrants, capacity, gender in classes:
                class_key = f"{course_name or 'General'} - {room_name} - {schedule}"
                availability = f"({registrants}/{capacity})"
                gender_info = f"[{gender}]" if gender else ""

                display_text = f"{class_key} {availability} {gender_info}"

                self.class_dict[display_text] = {
                    'timeslot_id': timeslot_id,
                    'room_id': room_id,
                    'schedule': schedule,
                    'room_name': room_name,
                    'course_name': course_name or 'General',
                    'registrants': registrants,
                    'capacity': capacity,
                    'gender': gender
                }
                self.class_options.append(display_text)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load form data: {e}")
            self.person_dict = {}
            self.person_options = []
            self.class_dict = {}
            self.class_options = []

    def show_class_details(self, event=None):
        """Show details of selected class"""
        class_selection = self.entries['class'].get()
        if class_selection in self.class_dict:
            class_info = self.class_dict[class_selection]
            details = (f"Course: {class_info['course_name']}\n"
                       f"Room: {class_info['room_name']}\n"
                       f"Schedule: {class_info['schedule']}\n"
                       f"Current Registrations: {class_info['registrants']}/{class_info['capacity']}\n"
                       f"Gender Restriction: {class_info['gender'] or 'No restriction'}")

            self.class_details_label.config(text=details, justify=tk.LEFT)

    def populate_form(self):
        """Populate form with existing registration data"""
        if self.registration_data:
            # Find and set person
            person_id = self.registration_data['person_id']
            for option, pid in self.person_dict.items():
                if pid == person_id:
                    self.entries['person'].set(option)
                    break

            # Find and set class
            timeslot_id = self.registration_data['timeslot_id']
            room_id = self.registration_data['room_id']

            for option, class_info in self.class_dict.items():
                if (class_info['timeslot_id'] == timeslot_id and
                        class_info['room_id'] == room_id):
                    self.entries['class'].set(option)
                    self.show_class_details()
                    break

    def save_registration(self):
        """Save registration data with validation"""
        try:
            # Get and validate form data
            person_selection = self.entries['person'].get().strip()
            class_selection = self.entries['class'].get().strip()

            # Validation
            if not all([person_selection, class_selection]):
                messagebox.showerror("Validation Error", "All fields are required!")
                return

            # Get IDs from selections
            if person_selection not in self.person_dict:
                messagebox.showerror("Validation Error", "Please select a valid person!")
                return
            person_id = self.person_dict[person_selection]

            if class_selection not in self.class_dict:
                messagebox.showerror("Validation Error", "Please select a valid class!")
                return

            class_info = self.class_dict[class_selection]
            timeslot_id = class_info['timeslot_id']
            room_id = class_info['room_id']

            # Check class capacity
            if class_info['registrants'] >= class_info['capacity']:
                if not self.registration_data:  # Only check for new registrations
                    messagebox.showerror("Class Full", "This class is already at full capacity!")
                    return

            # Check if person is already registered for this class
            if not self.registration_data:  # Only check for new registrations
                self.parent.parent.cursor.execute("""
                    SELECT COUNT(*) FROM registers_for 
                    WHERE person_id = %s AND timeslot_id = %s AND room_id = %s
                """, (person_id, timeslot_id, room_id))

                if self.parent.parent.cursor.fetchone()[0] > 0:
                    messagebox.showerror("Already Registered",
                                         "This person is already registered for this class!")
                    return

            # Database operations
            if self.registration_data:  # Edit existing registration
                old_person_id = self.registration_data['person_id']
                old_timeslot_id = self.registration_data['timeslot_id']
                old_room_id = self.registration_data['room_id']

                # Delete old registration
                self.parent.parent.cursor.execute("""
                    DELETE FROM registers_for 
                    WHERE person_id = %s AND timeslot_id = %s AND room_id = %s
                """, (old_person_id, old_timeslot_id, old_room_id))

                # Insert new registration
                self.parent.parent.cursor.execute("""
                    INSERT INTO registers_for (person_id, timeslot_id, room_id) 
                    VALUES (%s, %s, %s)
                """, (person_id, timeslot_id, room_id))

                success_msg = "Registration updated successfully!"
            else:  # Add new registration
                self.parent.parent.cursor.execute("""
                    INSERT INTO registers_for (person_id, timeslot_id, room_id) 
                    VALUES (%s, %s, %s)
                """, (person_id, timeslot_id, room_id))

                success_msg = "Registration added successfully!"

            self.parent.parent.connection.commit()
            messagebox.showinfo("Success", success_msg)
            self.parent.refresh_registrations()
            self.window.destroy()

        except Exception as e:
            self.parent.parent.connection.rollback()
            messagebox.showerror("Database Error", f"Failed to save registration: {e}")


# Main execution
if __name__ == "__main__":
    app = SportClubGUI()
    app.run()