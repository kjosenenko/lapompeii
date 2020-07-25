export class TextArea {
    userId: number;
    id: number;
    textArea: string;
    editMode: boolean;

    constructor(
        userId: number,
        id: number,
        textArea: string,
        editMode: boolean
    ) {
        this.userId = userId;
        this.id = id;
        this.textArea = textArea;
        this.editMode = editMode;
    }
}