import { Component, OnInit } from '@angular/core';
import { NewEmail } from '../../models/email.model';
import { Subscription } from 'rxjs';
import { ApiService } from '../../api.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {

  emails_list_subscription: Subscription;
  emails_list = [];
  email = new NewEmail('name', 'email', 'comment', 'phone');
  error = '';
  success = '';

  constructor(public api: ApiService) { 
    this.api.getEmails()
  }

  ngOnInit() {
    console.log('NgOnInit')
    this.emails_list_subscription = this.api.getEmailsList().subscribe(emails_list => {
      this.emails_list = emails_list;
    });
  }

  addEmail(email) {
    email.phone = '+1' + email.phone;
    this.success = 'Sending message...';
    this.api.addEmailService(email).then(results => {
      this.success = 'Thank you for your feedback.  We will respond to any inquiries ASAP';
      this.error = '';
    },
    err => {
      this.error = 'Please make sure all required fields are correctly filled in.';
      this.success = '';
    });
  }
}
