import { Component, OnInit } from '@angular/core';
import { NewItem } from '../../models/menu.model';
import { ApiService } from '../../api.service';
import { Subscription } from 'rxjs';
import {NgbModal, ModalDismissReasons} from '@ng-bootstrap/ng-bootstrap';
import { AuthService } from '../../auth.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  closeResult = '';
  slices_list_subscription: Subscription;
  slices_list = [];
  calzones_list_subscription: Subscription;
  calzones_list = [];
  pies_list_subscription: Subscription;
  pies_list = [];
  menu_categories_list_subscription: Subscription;
  menu_categories_list = [];
  menu_tags_list_subscription: Subscription;
  menu_tags_list = [];
  new_item = new NewItem('name', 'description', 'price', 'category', 'tags',);


  constructor(private modalService: NgbModal, public api: ApiService, public auth: AuthService) { 
    this.api.getSlices()
    this.api.getCalzones()
    this.api.getPies()
    this.api.getMenuCategories()
    this.api.getTags()
  }

  ngOnInit() {
    this.menu_tags_list_subscription = this.api.getTagsList().subscribe(menu_tags_list => {
      this.menu_tags_list = menu_tags_list;
    });
    this.slices_list_subscription = this.api.getSlicesList().subscribe(slices_list => {
      this.slices_list = slices_list;
    });
    this.calzones_list_subscription = this.api.getCalzonesList().subscribe(calzones_list => {
      this.calzones_list = calzones_list;
    });
    this.pies_list_subscription = this.api.getPiesList().subscribe(pies_list => {
      this.pies_list = pies_list;
    });
    this.menu_categories_list_subscription = this.api.getMenuCategoriesList().subscribe(menu_categories_list => {
      this.menu_categories_list = menu_categories_list;
    });
  }

  TagName(tag_id) {
    for (var this_tag of this.menu_tags_list) {
      if (this_tag.id == tag_id) {
        return this_tag.name;
      }
    }
  }

  TagId(tag_name) {
    for (var this_tag of this.menu_tags_list) {
      if (this_tag.name == tag_name) {
        return this_tag.id;
      }
    }
  }

  CategoryId(category_name) {
    for (var this_category of this.menu_categories_list) {
      if (this_category.name == category_name) {
        return this_category.id;
      }
    }
  }

  addItem(item) {
    item.category = this.CategoryId(item.category);
    if (item.tags) {
      var tags = [];
    for (var tag of item.tags) {
      tags.push(this.TagId(tag));
    }
    item.tags = tags
    }
    this.api.addMenuItemService(item),
    this.new_item = new NewItem('name', 'description', 'price', 'category', 'tags',);
  }

  deleteItem(item) {
    this.api.deleteMenuItemService(item)
  }

  updateItem(item) {
    this.api.updateMenuItemService(item)
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
