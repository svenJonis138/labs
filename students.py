from dataclasses import dataclass
# above import statement  and annotation below added to use the dataclass decorator


@dataclass
class Student:
    # removed the init and changed below to reflect the data types and added the gpa
    name: str
    school_id: str
    gpa: float

    def __str__(self):
        return f'Student: {self.name} School ID: {self.school_id} GPA: {self.gpa} '


def main():
    # main function to add test data. I much prefer some aspects of the dataclass syntax
    # but I definitely prefer a formatted string for output, so I put that back
    sven = Student('Sven Jonis', '1138', 3.81)
    sean = Student('Sean Jonze', '2323', 1.83)
    shawn = Student('Shawn Jones', '0666', 4.0)
    print(sven)
    print(sean)
    print(shawn)


main()