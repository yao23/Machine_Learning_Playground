rank_list = ["Responder", "Manager", "Director"]


class Call:
    """
    Represents a call from a user. Calls have a minimum rank and are assigned to the
    first employee who can handle that call.
    """
    def __init__(self, caller):
        self.__caller = caller  # Person who is calling.
        self.__rank = rank_list[0]  # Responder
        self.__handler = None  # Employee who is handling call.

    def set_handler(self, employee):
        """
        Set employee who is handling call.

        :param employee:
        :return:
        """
        self.__handler = employee

    def reply(self, message):
        """
        :param message:
        :return:

        Play recorded message to the customer.
        """
        print(message)

    def get_rank(self):
        return self.__rank

    def set_rank(self, rank):
        self.__rank = rank

    def increment_rank(self):
        if self.__rank == rank_list[0]:  # Responder
            self.__rank = rank_list[1]  # Manager
        elif self.__rank == rank_list[1]:  # Manager
            self.__rank = rank_list[2]  # Director
        return self.__rank

    def disconnect(self):
        """
        Disconnect call

        :return:
        """
        self.reply("Thank you for calling")


class Employee:
    """
    Employee is a super class for the Director, Manager, and Respondent classes. It is implemented as an
    abstract class, since there should be no reason to instantiated an Employee type directly.
    """
    def __init__(self):
        self.__current_call = None
        self._rank = rank_list[0]

    def receive_call(self, call):
        """
        Start the conversation

        :param call:
        :return:
        """
        self.__current_call = call

    def call_completed(self):
        """
        the issue is resolved, finish the call

        :return:
        """
        if self.__current_call is not None:
            # Disconnect the call.
            self.__current_call.disconnect()

            # Free the employee
            self.__current_call = None

        # Check if there is a call waiting in queue
        self.assign_new_call()

    def escalate_and_reassign(self):
        """
        The issue has not been resolved. Escalate the call, and assign a new call
        to the employee.

        :return:
        """
        if self.__current_call is not None:
            # escalate call
            self.__current_call.increment_rank()
            CallHandler.get_instance().dispatch_call(self.__current_call)

            # free the employee
            self.__current_call= None

        # assign a new call
        self.assign_new_call()

    def assign_new_call(self):
        """
        Assign a new call to an employee, if the employee is free.

        :return:
        """
        if not self.is_free():
            return False
        else:
            return CallHandler.get_instance().assignCall(self)

    def is_free(self):
        """
        Returns whether or not the employee is free.

        :return:
        """
        return self.__current_call is None

    def get_rank(self):
        return self._rank


class Respondent(Employee):
    def __init__(self):
        super(Respondent, self).__init__()
        self._rank = rank_list[0]  # Responder


class Manager(Employee):
    def __init__(self):
        super(Manager, self).__init__()
        self._rank = rank_list[1]  # Manager


class Director(Employee):
    def __init__(self):
        super(Director, self).__init__()
        self._rank = rank_list[2]  # Director


class Caller:
    """
    Caller
    """
    def __init__(self, user_id, name):
        self.name = name
        self.user_id = user_id


class CallHandler:
    """
    CallHandler is implement as a singleton class. It represents the body of the program,
    and all calls are funneled first through it.
    """
    def __init__(self):
        self.__instance = None
        self.__level = 3
        self.__num_respondent = 10
        self.__num_manager = 4
        self.__num_director = 2
        self.employee_levels = [None] * self.__level
        self.call_queues = [None] * self.__level

        # Create respondents.
        respondents =  [Respondent() for _ in range(self.__num_respondent)]
        self.employee_levels.append(respondents)

        # Create managers.
        managers = [Manager() for _ in range(self.__num_manager)]
        self.employee_levels.append(managers)

        # Create directors.
        directors = [Director() for _ in range(self.__num_director)]
        self.employee_levels.append(directors)

    def get_instance(self):
        """
        Get instance of singleton class.

        :return:
        """
        if self.__instance is None:
            self.__instance = CallHandler()
        return self.__instance

    def get_handler_for_call(self, call):
        """
        Gets the first available employee who can handle this call.

        :param call:
        :return:
        """
        for level in range(call.get_rank().get_value(), self.__level - 1):
            employee_level = self.employee_levels.get(level)
            for emp in employee_level:
                if emp.is_free():
                    return emp
        return None

    def dispatch_call_caller(self, caller):
        """
        Routes the call to an available employee, or saves in a queue if no employee available.

        :param caller:
        :return:
        """
        call = Call(caller)
        self.dispatch_call(call)

    def dispatch_call(self, call):
        """
        Routes the call to an available employee, or saves in a queue if no employee available.

        :param call:
        :return:
        """
        # Try to route the call to an employee with minimal rank.
        emp = self.get_handler_for_call(call)
        if emp is not None:
            emp.receive_call(call)
            call.set_handler(emp)
        else:
            # Place the call into corresponding call queue according to its rank.
            call.reply("Please wait for free employee to reply")
            self.call_queues.get(call.get_rank().get_value()).append(call)

    def assign_call(self, emp):
        """
        An employee got free. Look for a waiting call that he/she can serve. Return true
        if we were able to assign a call, false otherwise.

        :param emp:
        :return:
        """
        # Check the queues, starting from the highest rank this employee can serve.
        for rank in range(emp.get_rank().get_value(), -1, -1):
            que = self.call_queues.get(rank)

            # Remove the first call, if any
            if que.size() > 0:
                call = que.remove(0)
                if call is not None:
                    emp.receive_call(call)
                    return True
        return False


class CallCenter:
    def __init__(self):
        ch = CallHandler.get_instance()
