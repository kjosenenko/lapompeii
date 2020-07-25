import { Component, OnInit, Injectable } from '@angular/core';
import { NewEvent } from '../../models/event.model';
import { Subscription } from 'rxjs';
import { ApiService } from '../../api.service';
import {NgbModal, ModalDismissReasons, NgbDateAdapter, NgbDateStruct, NgbTimeStruct, NgbTimeAdapter} from '@ng-bootstrap/ng-bootstrap';
import { AuthService } from '../../auth.service';

const pad = (i: number): string => i < 10 ? `0${i}` : `${i}`;

@Injectable()
export class CustomAdapter extends NgbDateAdapter<string> {

  readonly DELIMITER = '-';

  fromModel(value: string | null): NgbDateStruct | null {
    if (value) {
      let date = value.split(this.DELIMITER);
      return {
        day : parseInt(date[0], 10),
        month : parseInt(date[1], 10),
        year : parseInt(date[2], 10)
      };
    }
    return null;
  }

  toModel(date: NgbDateStruct | null): string | null {
    return date ? date.year + this.DELIMITER + date.month + this.DELIMITER + date.day : null;
  }
}

export class NgbTimeStringAdapter extends NgbTimeAdapter<string> {

  fromModel(value: string| null): NgbTimeStruct | null {
    if (!value) {
      return null;
    }
    const split = value.split(':');
    return {
      hour: parseInt(split[0], 10),
      minute: parseInt(split[1], 10),
      second: parseInt(split[2], 10)
    };
  }

  toModel(time: NgbTimeStruct | null): string | null {
    return time != null ? `${pad(time.hour)}:${pad(time.minute)}:${pad(time.second)}` : null;
  }
}

@Component({
  selector: 'app-find-us',
  templateUrl: './find-us.component.html',
  styleUrls: ['./find-us.component.css'],

  providers: [
    {provide: NgbDateAdapter, useClass: CustomAdapter},
    {provide: NgbTimeAdapter, useClass: NgbTimeStringAdapter}
  ]
})

export class FindUsComponent implements OnInit {

  events_list_subscription: Subscription;
  events_list = [];
  closeResult = '';
  hourStep = 1;
  minuteStep = 30;
  meridian = true;
  model = new NewEvent('location', 'description', 'new Date()', 'startTime', 'new Date()', 'endTime');

  // TO DOs: cleanup CSS on forms so that datepickers line up with timepickers
  //         fix UI on update modal so that returned events are only updated from DB not incomplete form submission
  //         add form validation for required fields on new event form

  constructor(private modalService: NgbModal, public api: ApiService, public auth: AuthService) { 
      this.api.getSchedule()
  }

  ngOnInit() {
    console.log('NgOnInit')
    this.events_list_subscription = this.api.getEventsList().subscribe(events_list => {
      this.events_list = events_list;
    });
  }

  toggleMeridian() {
    this.meridian = !this.meridian;
  }

  startTime(event) {
    let newTime = event.start_date + " " + event.start_time;
    return newTime;
  }

  endTime(event) {
    let newTime = event.end_date + " " + event.end_time;
    return newTime;
  }

  addEvent(ngModel) {
    this.api.addEventService(ngModel),
    this.model = new NewEvent('location', 'description', 'new Date()', 'startTime', 'new Date()', 'endTime');
  }

  updateEvent(event) {
    this.api.updateEventService(event)
  }

  deleteEvent(event) {
    this.api.deleteEventService(event)
  }

  open(content) {
    this.modalService.open(content, {ariaLabelledBy: 'modal-basic-title'}).result.then((result) => {
      this.closeResult = `Closed with: ${result}`;
    }, (reason) => {
      this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
    });
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return `with: ${reason}`;
    }
  }
}


