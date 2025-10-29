# Web Development Services Website

A simple, minimal website for web development services with Firebase backend and Tailwind CSS.

## Features

- Clean, responsive design with Tailwind CSS
- Pricing sections (Minimum, Common, Mobile App packages)
- Contact form with Firebase integration
- Form submissions stored in Firestore

## Firebase Setup Instructions

To make the contact form work, you need to set up Firebase:

### 1. Create Firebase Project
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project"
3. Enter project name (e.g., "webdev-services")
4. Follow the setup wizard

### 2. Enable Firestore
1. In your Firebase project, go to "Firestore Database"
2. Click "Create database"
3. Start in test mode (for development)
4. Choose a location close to you

### 3. Get Firebase Configuration
1. Go to Project Settings (gear icon)
2. Scroll down to "Your apps"
3. Click "Web" icon to add a web app
4. Register your app (name it "WebDev Services")
5. Copy the Firebase configuration object

### 4. Update Firebase Config in index.html
Replace the placeholder values in `index.html` with your actual Firebase config:

```javascript
const firebaseConfig = {
    apiKey: "your-actual-api-key",
    authDomain: "your-project-id.firebaseapp.com",
    projectId: "your-actual-project-id",
    storageBucket: "your-project-id.appspot.com",
    messagingSenderId: "your-actual-sender-id",
    appId: "your-actual-app-id"
};
```

### 5. Set Up Email Notifications (Optional)

To receive email notifications when someone submits the form:

#### Option A: Use Firebase Functions (Recommended)
1. Install Firebase CLI: `npm install -g firebase-tools`
2. Login: `firebase login`
3. Initialize functions: `firebase init functions`
4. Create a function that sends emails when new contacts are added

#### Option B: Use Email Service Integration
You can integrate with services like:
- SendGrid
- Mailgun
- Nodemailer with Gmail

## Deployment

You can deploy this website to:
- Firebase Hosting (recommended)
- Netlify
- Vercel
- Any static hosting service

### Deploy to Firebase Hosting
1. Install Firebase CLI: `npm install -g firebase-tools`
2. Login: `firebase login`
3. Initialize hosting: `firebase init hosting`
4. Deploy: `firebase deploy`

## Customization

- Update pricing and package details in the HTML
- Modify colors and styling in Tailwind classes
- Add your own branding and content
- Update the contact information and business details

## Security Notes

- For production, set up proper Firestore security rules
- Consider adding reCAPTCHA to prevent spam
- Set up proper authentication if needed
