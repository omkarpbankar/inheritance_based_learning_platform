class User:
    def __init__(self, user_id, name, email):
        """Common properties for all users."""
        self.user_id = user_id
        self.name = name
        self.email = email

    def login(self):
        """Common functionality for all users."""
        print(f"{self.name} has logged in.")

    def logout(self):
        """Common functionality for all users."""
        print(f"{self.name} has logged out.")
        
    def get_role(self):
        return "Generic User"

    def display_info(self):
        """Displays common user info. Will be overridden by child classes."""
        print(f"ID: {self.user_id}, Name: {self.name}, Email: {self.email}, Role: {self.get_role()}")


class Student(User):
    def __init__(self, user_id, name, email, enrolled_courses=None):
        super().__init__(user_id, name, email)
        self.enrolled_courses = enrolled_courses if enrolled_courses else []

    def get_role(self):
        """Method Overriding: Changes the role returned for a Student."""
        return "Student"

    def enroll(self, course):
        """Role-specific functionality for Student."""
        self.enrolled_courses.append(course)
        print(f"{self.name} enrolled in {course}.")

    def display_info(self):
        """Method Overriding: Adds Student specific info to the display."""
        super().display_info()
        print(f"Enrolled Courses: {', '.join(self.enrolled_courses) if self.enrolled_courses else 'None'}")


class Mentor(User):
    def __init__(self, user_id, name, email, expertise=None):
        super().__init__(user_id, name, email)
        self.expertise = expertise if expertise else []

    def get_role(self):
        """Method Overriding: Changes the role returned for a Mentor."""
        return "Mentor"

    def create_course(self, course_name):
        """Role-specific functionality for Mentor."""
        print(f"{self.name} created a new course: {course_name}")

    def display_info(self):
        """Method Overriding: Adds Mentor specific info to the display."""
        super().display_info()
        print(f"Expertise: {', '.join(self.expertise) if self.expertise else 'None'}")


class Admin(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

    def get_role(self):
        """Method Overriding: Changes the role returned for an Admin."""
        return "Admin"

    def remove_user(self, user):
        """Role-specific functionality for Admin."""
        print(f"Admin {self.name} removed user {user.name} from the platform.")


# Demonstration
if __name__ == "__main__":
    student1 = Student(101, "Alice", "alice@example.com", ["Python 101"])
    mentor1 = Mentor(201, "Bob", "bob@example.com", ["Python", "Data Science"])
    admin1 = Admin(301, "Charlie", "charlie@admin.com")

    # Common functionality
    student1.login()
    mentor1.login()

    print("\n--- User Information ---")
    student1.display_info()
    print("-" * 20)
    mentor1.display_info()
    print("-" * 20)
    admin1.display_info()

    print("\n--- Role Specific Actions ---")
    student1.enroll("Advanced Python")
    mentor1.create_course("Machine Learning Basics")
    admin1.remove_user(student1)
