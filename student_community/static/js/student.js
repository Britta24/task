const studentEmail = localStorage.getItem("loggedIn");
if (!studentEmail) window.location.href = "login.html";

const nameInput = document.getElementById("name");
const collegeInput = document.getElementById("college");
const courseInput = document.getElementById("course");
const contactInput = document.getElementById("contact");
const skillsInput = document.getElementById("skills");
const resumeInput = document.getElementById("resume");
const resumeName = document.getElementById("resumeName");

const internshipsDiv = document.getElementById("internships");
const appsDiv = document.getElementById("applications");

function saveProfile() {

  if (!nameInput.value.trim()) {
    return alert("Name is required");
  }

  const profile = {
    name: nameInput.value.trim(),
    college: collegeInput.value,
    course: courseInput.value,
    contact: contactInput.value,
    skills: skillsInput.value,
    resume: resumeInput.files[0]?.name || resumeName.innerText
  };

  localStorage.setItem("studentProfile_" + studentEmail, JSON.stringify(profile));

  resumeName.innerText = profile.resume;

  alert("Profile saved");
}

function loadProfile() {

  const profile = JSON.parse(localStorage.getItem("studentProfile_" + studentEmail));
  if (!profile) return;

  nameInput.value = profile.name || "";
  collegeInput.value = profile.college || "";
  courseInput.value = profile.course || "";
  contactInput.value = profile.contact || "";
  skillsInput.value = profile.skills || "";
  resumeName.innerText = profile.resume || "";
}

function loadInternships() {

  const internships = JSON.parse(localStorage.getItem("internships")) || [];
  const apps = JSON.parse(localStorage.getItem("applications")) || [];

  if (!internships.length) {
    internshipsDiv.innerHTML = "<p>No internships available</p>";
    return;
  }

  internshipsDiv.innerHTML = "";

  internships.forEach(i => {

    const alreadyApplied = apps.some(
      a => a.student === studentEmail && a.internship === i.title
    );

    internshipsDiv.innerHTML += `
      <div class="card">
        <h4>${i.title}</h4>
        <p>Company: ${i.company}</p>

        <button class="btn" onclick="viewCompany('${i.company}')">
          View Company
        </button>

        <button class="btn" 
          ${alreadyApplied ? "disabled" : ""}
          onclick="apply('${i.title}','${i.company}')">
          ${alreadyApplied ? "Applied" : "Apply"}
        </button>
      </div>
    `;
  });
}

function viewCompany(companyName) {

  const companies = Object.keys(localStorage)
    .filter(k => k.startsWith("company_"))
    .map(k => JSON.parse(localStorage.getItem(k)));

  const company = companies.find(c => c.name === companyName);

  if (!company) return alert("Company profile not available");

  alert(`
Name: ${company.name}
Industry: ${company.industry}
Location: ${company.location}
Contact: ${company.contact}
About: ${company.about}
`);
}

function apply(title, company) {

  const profile = JSON.parse(localStorage.getItem("studentProfile_" + studentEmail));

  if (!profile || !profile.name) {
    return alert("Please complete and save your profile before applying");
  }

  const apps = JSON.parse(localStorage.getItem("applications")) || [];

  if (apps.some(a => a.student === studentEmail && a.internship === title))
    return alert("Already applied");

  apps.push({
    student: studentEmail,
    studentName: profile.name,
    internship: title,
    company: company,
    status: "Applied"
  });

  localStorage.setItem("applications", JSON.stringify(apps));

  loadInternships();
  loadApplications();
}

function loadApplications() {

  const apps = JSON.parse(localStorage.getItem("applications")) || [];

  appsDiv.innerHTML = "";

  const myApps = apps.filter(a => a.student === studentEmail);

  if (!myApps.length) {
    appsDiv.innerHTML = "<p>No applications yet</p>";
    return;
  }

  myApps.forEach(a => {

    appsDiv.innerHTML += `
      <div class="card">
        <b>${a.internship}</b>
        <p>Company: ${a.company}</p>
        <p>Status: ${a.status}</p>
      </div>
    `;
  });
}

function logout() {
  localStorage.removeItem("loggedIn");
  window.location.href = "index.html";
}

loadProfile();
loadInternships();
loadApplications();