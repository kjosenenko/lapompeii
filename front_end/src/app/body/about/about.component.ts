import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { ApiService } from '../../api.service';
import { AuthService } from '../../auth.service';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {

  text_areas_list_subscription: Subscription;
  text_areas_list = [];

  constructor(public api: ApiService, public auth: AuthService) {
      this.api.getTextAreas()
  }

  ngOnInit() {
    this.text_areas_list_subscription = this.api.getTextAreasList().subscribe(text_areas_list => {
      this.text_areas_list = text_areas_list;
    });
  }

  updateTextArea(text) {
    this.api.updateTextAreaService(text)
  }

  toggleEdit(text) {
    text.editMode = !text.editMode;
  }

}
