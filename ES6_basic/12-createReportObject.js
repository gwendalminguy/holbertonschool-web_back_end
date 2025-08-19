export default function createReportObject(employeesList) {
  const obj = {
    allEmployees: employeesList,
    getNumberOfDepartments(departments) {
      return Object.keys(departments).length;
    },
  };

  return obj;
}
