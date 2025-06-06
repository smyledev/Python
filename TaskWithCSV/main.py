# import os
from sys import argv

class Worker:

    def __init__(self, worker_data: [], struct_of_data: []):
        for i in range(0, len(struct_of_data)):
            cur_struct = struct_of_data[i]
            cur_struct = cur_struct.replace('\n', '')
            if cur_struct == "salary" or cur_struct == "rate":
               cur_struct = "hourly_rate"

            setattr(self, cur_struct, worker_data[i])

    def __str__(self):
        return f"Id:{self.id}, email:{self.email}, name:{self.name}, " \
               f"department:{self.department}, hours worked: {self.hours_worked}, " \
               f"hourly rate:{self.hourly_rate}"
 

params = argv
files = []
type_of_task = ""
for param in params:
    if ".csv" in param:
        files.append(param)
    elif "--report" in param:
        type_of_task = "report"

workers = []

for file in files:
    # if os.path.isfile(file):
    try:
        with open(file, "r") as file_readed:
            contents = file_readed.readlines()
            workers_data = contents[1:]
            for worker_data in workers_data:
                line_split = worker_data.split(",")
                for i in range(0, len(line_split)):
                    line_split[i] = line_split[i].replace('\n', '')
                new_worker = Worker(line_split, contents[0].split(","))
                workers.append(new_worker)
    except FileNotFoundError:
        print(f"Error: File -{file} not found")
        # exit()
    except Exception as e:
        print("Error: smth went wrong")

if len(workers) > 0 and type_of_task == "report":
    departments = []
    max_len_department = 0
    max_len_name = 0
    max_len_hours = 0
    max_len_rate = 0
    for cur_worker in workers:
        if cur_worker.department not in departments:
            departments.append(cur_worker.department)

        if max_len_department < len(cur_worker.department):
            max_len_department = len(cur_worker.department)
        if max_len_name < len(cur_worker.name):
            max_len_name = len(cur_worker.name)
        if max_len_hours < len(cur_worker.hours_worked):
            max_len_hours = len(cur_worker.hours_worked)
        if max_len_rate < len(cur_worker.hourly_rate):
            max_len_rate = len(cur_worker.hourly_rate)

    space_department = " "
    space_name = " "
    space_hours = " "
    space_rate = " "
    space_department_hyphen = "-"
    if (max_len_department > 0):
        space_department = " " * (max_len_department + 7)
        space_department_hyphen = "-" * (max_len_department + 5) + "  "
    if (max_len_name > 4):
        space_name = " " * (max_len_name - 5 + 2) 
    if (max_len_hours > 5):
        space_hours = " " * (max_len_hours - 5 + 2)
    if (max_len_rate > 4):
        space_rate = " " * (max_len_rate - 4 + 2)

    string_to_output = f"{space_department} name {space_name} hours {space_hours} rate {space_rate}payout"
    print(string_to_output)

    for department in departments:
        print(department)
        total_hours = 0
        total_payout = 0
        for cur_worker in workers:
            if cur_worker.department  == department:
                sum_of_work = int(cur_worker.hourly_rate) * int(cur_worker.hours_worked)
                total_hours += int(cur_worker.hours_worked)
                total_payout += sum_of_work
                space_name = " " * (max_len_name - len(cur_worker.name) + 2)
                space_hours = " " * (max_len_hours - len(cur_worker.hours_worked) + 2)
                space_rate = " " * (max_len_rate - len(cur_worker.hourly_rate) + 2)
                string_to_output = f"{space_department_hyphen} {cur_worker.name} {space_name}" \
                                   f"{cur_worker.hours_worked}   {space_hours}" \
                                   f"{cur_worker.hourly_rate} {space_rate} ${str(sum_of_work)}"
                print(string_to_output)

        space_name = " " * (max_len_name + 2)
        string_to_output = f"{space_department} {space_name} {str(total_hours)} {space_hours} " \
                           f"{space_rate}     ${str(total_payout)}"
        print(string_to_output)
else:
    print("No data was getting") 