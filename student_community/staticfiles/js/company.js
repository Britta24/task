const email = localStorage.getItem("loggedIn");
if (!email) window.location.href = "login.html";

const appsDiv = document.getElementById("applications");

function saveCompany() {

  const data = {
    name: cname.value,
    industry: industry.value,
    location: location.value,
    contact: contact.value,
    about: about.value
  };

  localStorage.setItem("company_" + email, JSON.stringify(data));

  alert("Company profile saved");
}

function loadCompany() {

  const data = JSON.parse(localStorage.getItem("company_" + email));
  if (!data) return;

  cname.value = data.name || "";
  industry.value = data.industry || "";
  location.value = data.location || "";
  contact.value = data.contact || "";
  about.value = data.about || "";
}

function postInternship() {

  const company = JSON.parse(localStorage.getItem("company_" + email));
  if (!company) return alert("Save company profile first");

  const internships = JSON.parse(localStorage.getItem("internships")) || [];

  internships.push({
    title: title.value,
    company: company.name
  });

  localStorage.setItem("internships", JSON.stringify(internships));

  title.value = "";

  alert("Internship posted");
}

function loadApplications() {

  const company = JSON.parse(localStorage.getItem("company_" + email));
  const apps = JSON.parse(localStorage.getItem("applications")) || [];

  const myApps = apps.filter(a => a.company === company?.name);

  appsDiv.innerHTML = myApps.length ? "" : "<p>No applications</p>";

  myApps.forEach((a, i) => {

    const student = JSON.parse(localStorage.getItem("studentProfile_" + a.student));

    appsDiv.innerHTML += `
      <div class="card">

        <h4>${a.internship}</h4>

        <p><b>Name:</b> ${a.studentName || student?.name || a.student}</p>
        <p><b>College:</b> ${student?.college || ""}</p>
        <p><b>Course:</b> ${student?.course || ""}</p>
        <p><b>Contact:</b> ${student?.contact || ""}</p>
        <p><b>Skills:</b> ${student?.skills || ""}</p>
        <p><b>Resume:</b> ${student?.resume || "Not uploaded"}</p>

        <select onchange="updateStatus(${i}, this.value)">
          <option ${a.status==="Applied"?"selected":""}>Applied</option>
          <option ${a.status==="Shortlisted"?"selected":""}>Shortlisted</option>
          <option ${a.status==="Rejected"?"selected":""}>Rejected</option>
          <option ${a.status==="Selected"?"selected":""}>Selected</option>
        </select>

      </div>
    `;
  });
}

function updateStatus(index, status) {

  const apps = JSON.parse(localStorage.getItem("applications"));

  const company = JSON.parse(localStorage.getItem("company_" + email));

  const myApps = apps.filter(a => a.company === company.name);

  const realIndex = apps.findIndex(a =>
    a.student === myApps[index].student &&
    a.internship === myApps[index].internship
  );

  apps[realIndex].status = status;

  localStorage.setItem("applications", JSON.stringify(apps));
}

function logout() {
  localStorage.removeItem("loggedIn");
  window.location.href = "index.html";
}

loadCompany();
loadApplications();