import { Injectable } from '@angular/core';
import { HttpClient } from  '@angular/common/http';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  API_URL = 'http://localhost:8000'
  private events = new Subject<any>();
  private textAreas = new Subject<any>();
  private slices = new Subject<any>();
  private calzones = new Subject<any>();
  private pies = new Subject<any>();
  private tags = new Subject<any>();
  private menuCategories = new Subject<any>();
  private emails = new Subject<any>();

  constructor(private  httpClient:  HttpClient) {
    // this.getSchedule();
    // this.getTextAreas();
  }

  getMenuCategoriesList(): Observable<any> {
    return this.menuCategories.asObservable();
  }

  getEventsList(): Observable<any> {
    return this.events.asObservable();
  }

  getTextAreasList(): Observable<any> {
    return this.textAreas.asObservable();
  }

  getTagsList(): Observable<any> {
    return this.tags.asObservable();
  }

  getSlicesList(): Observable<any> {
    return this.slices.asObservable();
  }

  getCalzonesList(): Observable<any> {
    return this.calzones.asObservable();
  }
  getPiesList(): Observable<any> {
    return this.pies.asObservable();
  }

  getEmailsList(): Observable<any> {
    return this.emails.asObservable();
  }

  getEmails() {
    return this.httpClient.get(this.API_URL + '/emails/?format=json').toPromise().then( results => {
      this.emails.next(results);
    });
  }

  addEmailService(email) {
    return this.httpClient.post(this.API_URL + '/emails/', email).toPromise().then( result => {
      return result;
    });        
  } 

  addMenuItemService(menuItem) {
    return this.httpClient.post(this.API_URL + '/menu_items/', menuItem).toPromise().then( result => {
      this.getPies(), this.getSlices(), this.getCalzones()
    }); 
  }

  deleteMenuItemService(menuItem) {
    return this.httpClient.delete(this.API_URL + '/menu_items/' + menuItem.id + '/').toPromise().then( result => {
      this.getPies(), this.getSlices(), this.getCalzones()
    });  
  }

  updateMenuItemService(menuItem) {
    return this.httpClient.post(this.API_URL + '/menu_items/' + menuItem.id + '/', menuItem).toPromise().then( result => {
      this.getPies(), this.getSlices(), this.getCalzones()
    }); 
  }

  getMenuCategories() {
    return this.httpClient.get(this.API_URL + '/menu_categories/?format=json').toPromise().then( results => {
      this.menuCategories.next(results);
    });    
  }

  getTags() {
    return this.httpClient.get(this.API_URL + '/menu_tags/?format=json').toPromise().then( results => {
      this.tags.next(results);
    });        
  }

  getSlices() {
    return this.httpClient.get(this.API_URL + '/menu_items/menucategories/1/?format=json').toPromise().then( results => {
      this.slices.next(results);
    });        
  }

  getCalzones() {
    return this.httpClient.get(this.API_URL + '/menu_items/menucategories/2/?format=json').toPromise().then( results => {
      this.calzones.next(results);
    });        
  }

  getPies() {
    return this.httpClient.get(this.API_URL + '/menu_items/menucategories/3/?format=json').toPromise().then( results => {
      this.pies.next(results);
    });        
  }

  getSchedule() {
    return this.httpClient.get(this.API_URL + '/schedule/?format=json').toPromise().then( results => {
      console.log(results)
      this.events.next(results);
    });    
  }

  addEventService(event) {
    return this.httpClient.post(this.API_URL + '/schedule/', event).toPromise().then( result => {
      this.getSchedule()
    });        
  } 
  
  updateEventService(event) {
    return this.httpClient.post(this.API_URL + '/schedule/' + event.id + '/', event).toPromise().then( result => {
      this.getSchedule()
    }); 
  }

  deleteEventService(event) {
    return this.httpClient.delete(this.API_URL + '/schedule/' + event.id + '/').toPromise().then( result => {
      this.getSchedule()
    });    
  }

  getTextAreas() {
    return this.httpClient.get(this.API_URL + '/text_areas/?format=json').toPromise().then( results => {
      this.textAreas.next(results);
    });    
  }

  updateTextAreaService(text) {
    return this.httpClient.post(this.API_URL + '/text_areas/' + text.id + '/', text).toPromise().then( result => {
      return result;
    }); 
  }
}

